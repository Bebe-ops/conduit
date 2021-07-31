from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# locators
registration_xp = '//li[@class="nav-item"]/a[@href="#/register"]'
sign_up_btn_xp = '//button[contains(text(),"Sign up")]'
notice_btn_xp = '//div[@class="swal-button-container"]/button'
logout_xp = '//nav/div/ul//li/a[@active-class="active"]'
login_xp = '//li[@class="nav-item"]/a[@href="#/login"]'
sign_in_btn_xp = '//button[contains(text(),"Sign in")]'


def find_elem_and_click(xp):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp))).click()


def fill_input_fields(my_list, field_list, xp):  # fill in input fields
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    time.sleep(3)
    driver.find_element_by_xpath(xp).click()


def notice_handling(expected_title, expected_text):  # validators
    notice_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
    notice_text = driver.find_element_by_xpath('//div[@class="swal-text"]')
    assert expected_title == notice_title.text and expected_text == notice_text.text
    find_elem_and_click(notice_btn_xp)


def check_input_fields_fill_in(fields):
    for _ in fields:
        assert _.get_attribute("value") != ""


def compare_the_values_of_two_lists(real_list, expected_list):
    for _ in range(len(real_list)):
        assert real_list[_].get_attribute("value") == expected_list[_]


# ----------------------------------------------------------------------------


# A007, CON_TC05_Felhasználói bejelentkezés nem létező felhasználóval
def test_login_validator1():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # locators, test data
    need_an_acc_xp = '//div/p/a[contains(text(),"Need an account?")]'
    expected_input_fields = ["Email", "Password"]
    expected_msg_title = 'Login failed!'
    expected_user_msg_text = 'Invalid user credentials.'
    random_user = f"Sanchez{randint(101, 200)}"
    reg_input_data = [f"{random_user}@gmail.com", "12ABab@&"]

    find_elem_and_click(login_xp)
    input_fields = driver.find_elements_by_tag_name("input")

    # check placeholders
    input_fields_placeholder_text = []
    for _ in input_fields:
        input_fields_placeholder_text.append(_.get_attribute("placeholder"))
    assert len(input_fields_placeholder_text) == 2
    assert expected_input_fields == input_fields_placeholder_text

    # check that the 2 input fields are displayed
    def displayed_and_enabled(xp):
        driver.find_element_by_xpath(xp)
        assert driver.find_element_by_xpath(xp).is_displayed()
        assert driver.find_element_by_xpath(xp).is_enabled()

    displayed_and_enabled(need_an_acc_xp)
    displayed_and_enabled(sign_in_btn_xp)

    # fill in input fields with test data
    fill_input_fields(reg_input_data, input_fields, sign_in_btn_xp)
    notice_handling(expected_msg_title, expected_user_msg_text)  # check --> error message title,text
    time.sleep(2)

    # check that the input fields are fill in with test_data
    check_input_fields_fill_in(input_fields)
    time.sleep(2)


# A008, CON_TC06_Felhasználói bejelentkezés helytelen formátumú email címmel
def test_login_validator2():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # test data
    user_data = ["tester@gmailcom", "12ABab#>"]
    expected_msg_title = 'Login failed!'
    expected_msg_email_format_text = 'Email must be a valid email.'

    find_elem_and_click(login_xp)
    input_fields = driver.find_elements_by_tag_name("input")
    fill_input_fields(user_data, input_fields, sign_in_btn_xp)
    time.sleep(2)

    # check -> input data is visible in the input fields
    compare_the_values_of_two_lists(input_fields, user_data)
    notice_handling(expected_msg_title, expected_msg_email_format_text)  # check validator
    time.sleep(2)
    check_input_fields_fill_in(input_fields)
    time.sleep(2)


# A009, CON_TC07_Felhasználói bejelentkezés regisztrált felhasználóval, de helytelen jelszóval
def test_login_validator3():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # test data
    random_user = f"Luke{randint(1, 100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]

    # successful registration
    find_elem_and_click(registration_xp)  # sign up
    time.sleep(2)
    reg_input_fields = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))
    fill_input_fields(reg_input_data, reg_input_fields, sign_up_btn_xp)

    find_elem_and_click(notice_btn_xp)
    time.sleep(2)
    find_elem_and_click(logout_xp)
    time.sleep(2)

    # login with wrong password
    # test_data
    expected_msg_title = 'Login failed!'
    expected_user_pwd_text = 'Invalid user credentials.'
    login_data = [reg_input_data[1], "44ABab@&"]

    find_elem_and_click(login_xp)
    time.sleep(2)
    log_input_fields = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))
    fill_input_fields(login_data, log_input_fields, sign_in_btn_xp)
    time.sleep(2)

    compare_the_values_of_two_lists(log_input_fields, login_data)
    notice_handling(expected_msg_title, expected_user_pwd_text)
    time.sleep(2)
    check_input_fields_fill_in(log_input_fields)

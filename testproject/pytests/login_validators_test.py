from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mód


def find_elem_and_click(xp):
    driver.find_element_by_xpath(xp).click()


def fill_input_fields(my_list, field_list, xp):  # fill in input fields
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    time.sleep(3)
    driver.find_element_by_xpath(xp).click()


def swal_handling(expected_title, expected_text):  # validators
    swal_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
    swal_text = driver.find_element_by_xpath('//div[@class="swal-text"]')
    assert expected_title == swal_title.text and expected_text == swal_text.text
    time.sleep(3)
    driver.find_element_by_xpath('//div[@class="swal-modal"]//button').click()


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
    time.sleep(3)

    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/login"]')
    input_fields = driver.find_elements_by_tag_name("input")
    expected_input_fields = ["Email", "Password"]
    input_fields_placeholder_text = []

    # check that the 2 input fields are displayed (+ placeholders)
    for _ in input_fields:
        input_fields_placeholder_text.append(_.get_attribute("placeholder"))
    assert len(input_fields_placeholder_text) == 2
    assert expected_input_fields == input_fields_placeholder_text

    # check need_an_account_link, sign_in_btn
    def displayed_and_enabled(xp):
        driver.find_element_by_xpath(xp)
        assert driver.find_element_by_xpath(xp).is_displayed()
        assert driver.find_element_by_xpath(xp).is_enabled()

    displayed_and_enabled('//div/p/a[contains(text(),"Need an account?")]')
    displayed_and_enabled('//button[contains(text(),"Sign in")]')

    # fill in input fields with test data
    random_user = f"Sancho{randint(101,200)}"
    reg_input_data = [f"{random_user}@gmail.com", "12ABab@&"]
    expected_msg_title = 'Login failed!'
    expected_user_msg_text = 'Invalid user credentials.'

    fill_input_fields(reg_input_data, input_fields, '//button[contains(text(),"Sign in")]')
    swal_handling(expected_msg_title, expected_user_msg_text)  # check --> error message title,text
    time.sleep(3)

    # check that the input fields are fill in with test_data
    check_input_fields_fill_in(input_fields)
    time.sleep(3)


# A008, CON_TC06_Felhasználói bejelentkezés helytelen formátumú email címmel
def test_login_validator2():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(3)

    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/login"]')
    time.sleep(2)
    input_fields = driver.find_elements_by_tag_name("input")
    user_data = ["wester@gmailcom", "12ABab#>"]
    expected_msg_title = 'Login failed!'
    expected_msg_email_format_text = 'Email must be a valid email.'

    fill_input_fields(user_data, input_fields, '//button[contains(text(),"Sign in")]')
    time.sleep(3)
    compare_the_values_of_two_lists(input_fields, user_data)  # check -> input data is visible in the input fields
    swal_handling(expected_msg_title, expected_msg_email_format_text)  # check validator
    time.sleep(3)
    check_input_fields_fill_in(input_fields)
    time.sleep(3)


# A009, CON_TC07_Felhasználói bejelentkezés regisztrált felhasználóval, de helytelen jelszóval
def test_login_validator3():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(3)

    # successful registration
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')  # sign up
    time.sleep(3)
    reg_input_fields = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))
    random_user = f"Lukas{randint(1,100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]

    fill_input_fields(reg_input_data, reg_input_fields, '//button[contains(text(),"Sign up")]')
    swal_btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              ((By.XPATH, '//div[@class="swal-button-container"]/button')))
    swal_btn.click()
    time.sleep(3)
    find_elem_and_click('//nav/div/ul//li/a[@active-class="active"]')  # logout
    time.sleep(3)

    # login with wrong password
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/login"]')
    time.sleep(2)

    expected_msg_title = 'Login failed!'
    expected_user_pwd_text = 'Invalid user credentials.'
    login_data = [reg_input_data[1], "44ABab@&"]
    log_input_fields = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))

    fill_input_fields(login_data, log_input_fields, '//button[contains(text(),"Sign in")]')
    time.sleep(3)
    compare_the_values_of_two_lists(log_input_fields, login_data)
    swal_handling(expected_msg_title, expected_user_pwd_text)
    time.sleep(3)
    check_input_fields_fill_in(log_input_fields)
    time.sleep(3)

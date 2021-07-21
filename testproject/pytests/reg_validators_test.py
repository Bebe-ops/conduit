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


def fill_input_fields(my_list, field_list):  # fill in registration form input fields
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    driver.find_element_by_xpath('//button[contains(text(),"Sign up")]').click()


def swal_handling(expected_title, expected_text):  # validators
    swal_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
    swal_text = driver.find_element_by_xpath('//div[@class="swal-text"]')
    assert expected_title == swal_title.text and expected_text == swal_text.text
    time.sleep(3)
    driver.find_element_by_xpath('//div[@class="swal-modal"]//button').click()


def check_input_fields_fill_in(field_list):
    for _ in field_list:
        assert _.get_attribute("value") == ""
# ---------------------------------------------------------------------------------


# A002, CON_TC24_Regisztráció validátorok ellenőrzése (üres form, helytelen formátumú password)
def test_registration_validator1():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(3)
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')  # sign up

    # check that the 3 input fields are displayed
    input_fields = driver.find_elements_by_tag_name("input")
    expected_input_fields = ["Username", "Email", "Password"]
    assert len(input_fields) == 3

    def compare_two_lists_items(real_list, attr, expected_list):  # check placeholders
        for _ in range(len(real_list)):
            assert real_list[_].get_attribute(attr) == expected_list[_]

    compare_two_lists_items(input_fields, "placeholder", expected_input_fields)

    # check have_an_account_link, sign_up_btn
    def displayed_and_enabled(xp):
        driver.find_element_by_xpath(xp)
        assert driver.find_element_by_xpath(xp).is_displayed()
        assert driver.find_element_by_xpath(xp).is_enabled()

    displayed_and_enabled('//div/p/a[contains(text(),"Have an account?")]')
    displayed_and_enabled('//button[contains(text(),"Sign up")]')

    # check password format validation message
    random_user = f"Test{randint(1,200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "ABCabc1"]
    expected_msg_title = 'Registration failed!'
    expected_msg_pwd_text = 'Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 ' \
                            'lowercase letter.'

    fill_input_fields(reg_input_data, input_fields)
    swal_handling(expected_msg_title, expected_msg_pwd_text)
    time.sleep(3)
    check_input_fields_fill_in(input_fields)

    # EMPTY FORM : check empty validation message
    expected_empty_form_msg_text = 'Username field required.'

    find_elem_and_click('//button[contains(text(),"Sign up")]')  # sign_up_btn.click
    swal_handling(expected_msg_title, expected_empty_form_msg_text)
    time.sleep(3)
    check_input_fields_fill_in(input_fields)


# A003, CON_TC03_Regisztráció validátorok ellenőrzése (regisztráció helytelen email formátummal)
def test_registration_validator2():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(3)
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')  # sign up
    time.sleep(3)
    random_user = f"Huanita{randint(4,100)}"
    reg_input_data = [random_user, f"{random_user}@gmailcom", "12ABab@&"]
    input_fields = driver.find_elements_by_tag_name("input")
    expected_msg_title = 'Registration failed!'
    expected_email_format_msg_text = 'Email must be a valid email.'

    fill_input_fields(reg_input_data, input_fields)
    swal_handling(expected_msg_title, expected_email_format_msg_text)  # check validator
    time.sleep(3)
    check_input_fields_fill_in(input_fields)



# A004, CON_TC23_Sikertelen regisztráció, már regisztrált email fiókkal
def test_registration_validator3():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(3)

    # successful registration
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')  # sign up
    time.sleep(3)

    random_user = f"Mary{randint(100, 200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]
    input_fields = driver.find_elements_by_tag_name("input")

    fill_input_fields(reg_input_data, input_fields)
    swal_btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              ((By.XPATH, '//div[@class="swal-button-container"]/button')))
    swal_btn.click()
    time.sleep(3)
    find_elem_and_click('//nav/div/ul//li/a[@active-class="active"]')  # logout
    time.sleep(3)

    # repeated registration
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')  # sign_up link
    time.sleep(3)
    fill_input_fields(reg_input_data, input_fields)
    time.sleep(5)

    expected_msg_title = 'Registration failed!'
    expected_email_msg_text = 'Email already taken.'

    swal_handling(expected_msg_title, expected_email_msg_text)  # check validator
    time.sleep(3)
    check_input_fields_fill_in(input_fields)


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


def find_elem_and_click(xp):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp))).click()


def find_elements(tag_name):
    elements = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, tag_name)))
    return elements


def fill_input_fields(my_list, field_list, xp):
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    time.sleep(3)
    find_elem_and_click(xp)

# -----------------------------------------------------------------------------------------


# A010, CON_TC04_Sikeres login(létező user)
def test_successful_login():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # locators
    registration_xp = '//li[@class="nav-item"]/a[@href="#/register"]'
    reg_input_fields_tag = 'input'
    sign_up_btn_xp = '//button[contains(text(),"Sign up")]'
    notice_btn_xp = '//div[@class="swal-button-container"]/button'
    logout_xp = '//nav/div/ul//li/a[@active-class="active"]'
    login_xp = '//li[@class="nav-item"]/a[@href="#/login"]'
    log_input_fields_tag = 'input'
    sign_in_btn_xp = '//button[contains(text(),"Sign in")]'
    nav_bar_links_xp = '//nav//div[@class="container"]/ul/li'

    # test_data
    random_user = f"Simone{randint(1, 100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]
    login_data = [reg_input_data[1], reg_input_data[2]]
    expected_login_nav_bar_elements = ['Home', ' New Article', ' Settings', reg_input_data[0], ' Log out']

    # successful registration
    find_elem_and_click(registration_xp)  # sign up
    time.sleep(2)

    reg_input_fields = find_elements(reg_input_fields_tag)
    fill_input_fields(reg_input_data, reg_input_fields, sign_up_btn_xp)
    find_elem_and_click(notice_btn_xp)

    time.sleep(2)
    find_elem_and_click(logout_xp)  # logout
    time.sleep(3)

    # successful login
    find_elem_and_click(login_xp)
    time.sleep(2)
    log_input_fields = find_elements(log_input_fields_tag)

    fill_input_fields(login_data, log_input_fields, sign_in_btn_xp)
    time.sleep(2)
    assert driver.current_url == 'http://localhost:1667/#/'

    nav_bar_links = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, nav_bar_links_xp)))

    # # check navbar elements
    for _ in range(len(nav_bar_links)):
        assert nav_bar_links[_].text == expected_login_nav_bar_elements[_]

    find_elem_and_click(logout_xp)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mód


# A006, CON_TC09_Logout
def test_logout():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(5)

    # registration and login
    def find_elem_and_click(xp):
        driver.find_element_by_xpath(xp).click()

    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')  # sign up
    time.sleep(3)
    nav_bar_links = driver.find_elements_by_xpath('//nav//div[@class="container"]/ul/li')
    random_user = f"Pete{randint(1,100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]
    expected_login_nav_bar_elements = ['Home', ' New Article', ' Settings', reg_input_data[0], ' Log out']
    input_fields = driver.find_elements_by_tag_name("input")

    def fill_input_fields(my_list):  # fill in registration form input fields
        for _ in range(len(my_list)):
            input_fields[_].send_keys(my_list[_])
        time.sleep(2)
        driver.find_element_by_xpath('//button[contains(text(),"Sign up")]').click()

    fill_input_fields(reg_input_data)
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="swal-modal"]//button').click()
    time.sleep(3)

    def compare_the_text_of_two_lists(real_list, expected_list):
        for _ in range(len(real_list)):
            assert real_list[_].text == expected_list[_]

    compare_the_text_of_two_lists(nav_bar_links, expected_login_nav_bar_elements)  # check login
    time.sleep(3)
    assert driver.current_url == 'http://localhost:1667/#/'

    # logout
    find_elem_and_click('//nav/div/ul//li/a[@active-class="active"]')
    expected_logout_nav_bar_elements = ['Home', 'Sign in', 'Sign up']
    time.sleep(2)

    def compare_the_text_of_two_lists(real_list, expected_list):
        for _ in range(len(real_list)):
            assert real_list[_].text == expected_list[_]

    compare_the_text_of_two_lists(nav_bar_links, expected_logout_nav_bar_elements)  # check logout
    driver.close()

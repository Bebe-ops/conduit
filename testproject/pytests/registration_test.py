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


# A005, CON_TC02_Sikeres regisztráció, még nem létező felhasználói adatokkal.
def test_registration():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(3)

    def find_elem_and_click(xp):
        driver.find_element_by_xpath(xp).click()

    # sign up
    find_elem_and_click('//li[@class="nav-item"]/a[@href="#/register"]')
    time.sleep(3)
    random_user = f"Mike{randint(1,200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]
    nav_bar_links = driver.find_elements_by_xpath('//nav//div[@class="container"]/ul/li')
    expected_login_nav_bar_elements = ['Home', ' New Article', ' Settings', reg_input_data[0], ' Log out']
    expected_msg_title_ok = 'Welcome!'
    expected_registration_successful = 'Your registration was successful!'
    input_fields = driver.find_elements_by_tag_name("input")

    def fill_input_fields(my_list):  # fill in registration form input fields
        for _ in range(len(my_list)):
            input_fields[_].send_keys(my_list[_])
        time.sleep(2)
        driver.find_element_by_xpath('//button[contains(text(),"Sign up")]').click()

    fill_input_fields(reg_input_data)

    def swal_handling(expected_title, expected_text):  # check validator
        swal_title = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        swal_text = driver.find_element_by_xpath('//div[@class="swal-text"]')
        assert expected_title == swal_title.text and expected_text == swal_text.text
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="swal-modal"]//button').click()

    swal_handling(expected_msg_title_ok, expected_registration_successful)
    time.sleep(3)

    def compare_the_text_of_two_lists(real_list, expected_list):
        for _ in range(len(real_list)):
            assert real_list[_].text == expected_list[_]

    compare_the_text_of_two_lists(nav_bar_links, expected_login_nav_bar_elements)  # check login

    time.sleep(3)
    find_elem_and_click('//nav/div/ul//li/a[@active-class="active"]')  # logout
    time.sleep(3)
    driver.close()

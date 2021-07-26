from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://localhost:1667")


class Registration:
    def __init__(self):
        self.reg_xp = '//li[@class="nav-item"]/a[@href="#/register"]'
        self.nav_bar_links_xp = '//nav//div[@class="container"]/ul/li'
        self.sign_up_btn_xp = '//button[contains(text(),"Sign up")]'
        self.logout_xp = '//nav/div/ul//li/a[@active-class="active"]'
        self.have_an_account_link_xp = '//div/p/a[contains(text(),"Have an account?")]'
        self.input_fields_tag_name = 'input'

        self.swal_title_xp = '//div[@class="swal-title"]'
        self.swal_text_xp = '//div[@class="swal-text"]'
        self.swal_btn_xp = '//div[@class="swal-modal"]//button'

    def locator(self, xp):
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp)))
        return element

    def locators(self, xp):
        element = driver.find_elements_by_xpath(xp)
        return element

    def locators_tag_name(self, tag):
        element = driver.find_elements_by_tag_name(tag)
        return element

    def fill_input_fields(self, my_list, field_list):  # fill in registration form input fields
        for _ in range(len(my_list)):
            field_list[_].send_keys(my_list[_])
        self.locator(self.sign_up_btn_xp).click()

    def swal_handling(self, expected_title, expected_text):  # check validator
        swal_title = self.locator(self.swal_title_xp)
        swal_text = self.locator(self.swal_text_xp)
        assert swal_title.text == expected_title and swal_text.text == expected_text
        time.sleep(3)
        self.locator(self.swal_btn_xp).click()

    def compare_the_text_of_two_lists(self, real_list, expected_list):
        for _ in range(len(real_list)):
            assert real_list[_].text == expected_list[_]

    def compare_two_lists_items(self, real_list, attr, expected_list):  # check placeholders
        for _ in range(len(real_list)):
            assert real_list[_].get_attribute(attr) == expected_list[_]

    def check_input_fields_fill_in(self, field_list):
        for _ in field_list:
            assert _.get_attribute("value") == ""

    def displayed_and_enabled(self, xp):
        driver.find_element_by_xpath(xp)
        assert driver.find_element_by_xpath(xp).is_displayed()
        assert driver.find_element_by_xpath(xp).is_enabled()

    def teardown(self):
        driver.close()

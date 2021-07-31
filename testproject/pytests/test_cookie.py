from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True


class TestCookie(object):
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver.get("http://localhost:1667")

    def teardown(self):
        self.driver.close()

    def test_cookie(self):
        def locators(xp):
            element = self.driver.find_element_by_xpath(xp)
            return element

        cookie = locators('//*[@class="cookie__bar__content"]//div')
        decline_btn = locators('//*[@id="cookie-policy-panel"]//button[1]/div')
        accept_btn = locators('//*[@id="cookie-policy-panel"]//button[2]/div')
        link = locators('//a[@href="https://cookiesandyou.com/"]')
        cookie_div_class_name = locators('//div[@class="cookie__bar__content"]').get_attribute('class')

        # test_data
        cookie_text = 'We use cookies to ensure you get the best experience on our website. Learn More...'
        decline_btn_text = 'I decline!'
        accept_btn_text = 'I accept!'

        assert cookie.is_displayed()
        assert cookie.text == cookie_text
        assert decline_btn.text == decline_btn_text
        assert accept_btn.text == accept_btn_text
        assert decline_btn.is_enabled()
        assert accept_btn.is_enabled()

        actual_all_div = []

        def find_all_div_class_name(my_list):
            all_div = self.driver.find_elements_by_tag_name('div')
            all_div_class_name = my_list
            for _ in all_div:
                all_div_class_name.append(_.get_attribute("class"))

        find_all_div_class_name(actual_all_div)
        assert cookie_div_class_name in actual_all_div
        time.sleep(3)

        main_window = self.driver.window_handles[0]
        link.click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(main_window)
        time.sleep(3)

        accept_btn.click()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)
        actual_all_div2 = []
        find_all_div_class_name(actual_all_div2)
        assert cookie_div_class_name not in actual_all_div2

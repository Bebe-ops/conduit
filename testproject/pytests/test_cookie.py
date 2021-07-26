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

        time.sleep(3)
        main_window = self.driver.window_handles[0]
        link.click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(main_window)
        time.sleep(3)

        decline_btn.click()
        time.sleep(5)

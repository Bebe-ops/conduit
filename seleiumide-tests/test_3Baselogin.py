# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

class Test3Baselogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validlogin(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(886, 782)
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Sign up\')]").click()
    elements = self.driver.find_elements(By.XPATH, "//h1[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Have an account?\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@type=\'text\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "(//input[@type=\'text\'])[2]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@type=\'password\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Huanita1")
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").click()
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("huanita1@gmail.com")
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("123ABCabc#&@{}í")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-title").text == "Welcome!"
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-text").text == "Your registration was successful!"
    self.driver.find_element(By.XPATH, "//button[contains(.,\'OK\')]").click()
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Huanita1\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\' Log out\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign in\')]")
    assert len(elements) == 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) == 0
    self.driver.find_element(By.XPATH, "//a[contains(.,\' Log out\')]").click()
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Sign in\')]").click()
    elements = self.driver.find_elements(By.XPATH, "//input[@type=\'text\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@type=\'password\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Sign in\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("huanita1@gmail.com")
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("123ABCabc#&@{}í")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign in\')]").click()
    WebDriverWait(self.driver, Huanita1).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(.,\'Huanita1\')]")))
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\' Log out\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign in\')]")
    assert len(elements) == 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) == 0
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
  
  def test_validloginjustlogin(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(886, 782)
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign in\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Sign in\')]").click()
    elements = self.driver.find_elements(By.XPATH, "//input[@type=\'text\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@type=\'password\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Sign in\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Dtesterbuggie@gmail.com")
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("123ABCabc#&@{}í")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign in\')]").click()
    WebDriverWait(self.driver, TesterD).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(.,\'TesterD\')]")))
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\' Log out\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign in\')]")
    assert len(elements) == 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) == 0
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
  

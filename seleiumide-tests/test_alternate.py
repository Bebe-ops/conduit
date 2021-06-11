# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAlternate():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_registrationwithanemailaddressalreadyregistered(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(886, 782)
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.XPATH, "//h1[contains(.,\'Sign up\')]").text == "Sign up"
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Have an account?\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").send_keys("TesterB71011")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").send_keys("70111testerbuggie@gmail.com")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").send_keys("123ABCabc#&@{}í")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-title").text == "Registration failed!"
    assert self.driver.find_element(By.XPATH, "//div/div[3]").text == "Email already taken."
    self.driver.find_element(By.XPATH, "//button[contains(.,\'OK\')]").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
    assert len(elements) > 0
  
  def test_registrationwithaninvalidemailaddress(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(886, 782)
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.XPATH, "//h1[contains(.,\'Sign up\')]").text == "Sign up"
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Have an account?\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").send_keys("Testregi")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").send_keys("testregigmail.som")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").send_keys("AsAs5678")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-title").text == "Registration failed!"
    assert self.driver.find_element(By.XPATH, "//div/div[3]").text == "Email must be a valid email."
    self.driver.find_element(By.XPATH, "//button[contains(.,\'OK\')]").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").send_keys("testregi")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").send_keys("testregi@gmailcom")
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").send_keys("AsAs5678")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-title").text == "Registration failed!"
    assert self.driver.find_element(By.XPATH, "//div/div[3]").text == "Email must be a valid email."
    self.driver.find_element(By.XPATH, "//button[contains(.,\'OK\')]").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
    assert len(elements) > 0
  
  def test_registrationwithemptyform(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(886, 782)
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.XPATH, "//h1[contains(.,\'Sign up\')]").text == "Sign up"
    elements = self.driver.find_elements(By.XPATH, "//a[contains(.,\'Have an account?\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Sign up\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input").click()
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign up\')]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-title").text == "Registration failed!"
    assert self.driver.find_element(By.CSS_SELECTOR, ".swal-text").text == "Username field required."
    self.driver.find_element(By.XPATH, "//button[contains(.,\'OK\')]").click()
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset/input")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[2]/input")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'app\']/div/div/div/div/form/fieldset[3]/input")
    assert len(elements) > 0
  

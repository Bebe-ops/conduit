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

reg_xp = '//li[@class="nav-item"]/a[@href="#/register"]'
nav_bar_links_xp = '//nav//div[@class="container"]/ul/li'
sign_up_btn_xp = '//button[contains(text(),"Sign up")]'
notice_btn_xp = '//div[@class="swal-modal"]//button'
settings_xp = '//a[contains(text(), "Settings")]'
settings_fields_xp = '//fieldset[@class="form-group"]/*'
update_settings_btn_xp = '//button[contains(text(), "Update Settings")]'
logout_xp = '//nav/div/ul//li/a[@active-class="active"]'
login_xp = '//*[@id="app"]/nav/div/ul/li[@class="nav-item"]/a[@href="#/login"]'
log_input_fields_xp = '//input'
sign_in_btn_xp = '//button[contains(text(),"Sign in")]'


def locator(xp):
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp)))
    return element


def locators(xp):
    element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, xp)))
    return element


def fill_input_fields(my_list, field_list, xp):
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    locator(xp).click()


def compare_the_text_of_two_lists(real_list, expected_list):
    for _ in range(len(real_list)):
        assert real_list[_].text == expected_list[_]


# A014_CON_TC21_Felhasználói profil szerkesztése
def test_user_profile():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(1)

    # registration
    # test data
    random_user = f"Bud{randint(1, 200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]
    expected_login_nav_bar_elements = ['Home', ' New Article', ' Settings', reg_input_data[0], ' Log out']

    locator(reg_xp).click()
    time.sleep(1)
    # locators(nav_bar_links_xp)
    input_fields = driver.find_elements_by_tag_name('input')
    time.sleep(1)
    fill_input_fields(reg_input_data, input_fields, sign_up_btn_xp)
    locator(notice_btn_xp).click()
    time.sleep(2)
    compare_the_text_of_two_lists(locators(nav_bar_links_xp), expected_login_nav_bar_elements)  # check login

    # modify user_profile data
    # test data
    random_user = f"Einstein{randint(1, 200)}"
    mod_data = {"pict_url": "https://cdn.pixabay.com/photo/2013/07/12/18/35/alien-153542_960_720.png",
                "username": f"{random_user}", "bio": "Theoretical physicist", "email": f"{reg_input_data[1]}",
                "pwd": f"{randint(10, 99)}VPab@&"}

    locator(settings_xp).click()
    settings_fields = locators(settings_fields_xp)
    mod_data_key_list = list(mod_data.values())

    for _ in range(len(settings_fields)):  # clear and fill fields
        settings_fields[_].clear()
        settings_fields[_].send_keys(mod_data_key_list[_])

    locator(update_settings_btn_xp).click()
    time.sleep(2)
    locator(notice_btn_xp).click()

    # check user profile: picture, username in navbar
    user_id_nav_xp = f'//nav//li/a[contains(text(), "{mod_data["username"]}")]'
    profile_picture_xp = '//img[@class="user-img"]'
    assert locator(user_id_nav_xp).text == mod_data["username"]
    locator(user_id_nav_xp).click()
    time.sleep(3)
    assert locator(profile_picture_xp).get_attribute("src") == mod_data["pict_url"]
    time.sleep(2)

    # logout --> login with modified profile data
    locator(logout_xp).click()
    time.sleep(1)
    locator(login_xp).click()
    log_input_fields = locators(log_input_fields_xp)
    mod_data_keys = [mod_data["email"], mod_data["pwd"]]
    time.sleep(1)
    fill_input_fields(mod_data_keys, log_input_fields, sign_in_btn_xp)
    time.sleep(2)

    # check profile data
    locator(settings_xp).click()
    time.sleep(2)

    for _ in range(len(settings_fields)):
        if settings_fields[_] == locator('//input[@type="password"]'):
            continue
        else:
            assert settings_fields[_].get_attribute("value") == mod_data_key_list[_]

    # logout
    locator(logout_xp).click()

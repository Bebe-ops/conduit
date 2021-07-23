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
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mód


def find_elem_and_click(xp):
    driver.find_element_by_xpath(xp).click()


def fill_input_fields(my_list, field_list, btn):
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    btn.click()


def compare_the_values_of_two_lists(real_list, expected_list, attr):
    for _ in range(len(real_list)):
        assert real_list[_].get_attribute(attr) == expected_list[_]


def create_text_list(real_list, new_list):
    for _ in real_list:
        new_list.append(_.text)
# ------------------------------------------------------------------------------------------


# A011_CON_TC10_Új blogbejegyzés (minden mező kitöltése)
def test_new_blog():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(5)

    # successful registration
    sign_up = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, '//li[@class="nav-item"]/a[@href="#/register"]')))
    sign_up.click()
    time.sleep(3)
    reg_input_fields = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))
    random_user = f"Pedro{randint(1, 100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]

    # ---------------------------fill input field, and get test data ----------------------------------
    reg_data = []

    def fill_input_and_get_data(my_list, field_list):
        for _ in range(len(my_list)):
            field_list[_].send_keys(my_list[_])

    fill_input_and_get_data(reg_input_data, reg_input_fields)
    time.sleep(5)

    def create_attr_list(real_list, new_list):
        for _ in real_list:
            new_list.append(_.get_attribute("value"))

    create_attr_list(reg_input_fields, reg_data)
    time.sleep(5)

    # writing test data to a file
    with open("login_data.txt", "w") as login_file:  # write data_list in file
        for item in reg_data:
            login_file.write("%s\n" % item)

    time.sleep(5)
    driver.find_element_by_xpath('//button[contains(text(),"Sign up")]').click()
    # ----------------------------------------------------------------------------------------------
    swal_btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              ((By.XPATH, '//div[@class="swal-button-container"]/button')))
    swal_btn.click()
    time.sleep(5)

    # new blog_post
    find_elem_and_click('//a[@href="#/editor"]')  # editor
    time.sleep(5)
    form_input_fields = driver.find_elements_by_xpath('//form/fieldset//fieldset//input')
    textarea = driver.find_element_by_tag_name('textarea')
    publish_btn = driver.find_element_by_xpath('//form/button')
    form_input_fields.insert(2, textarea)

    # check placeholders
    except_elements_placeholder = ["Article Title", "What's this article about?", "Write your article (in markdown)",
                                   "Enter tags"]
    compare_the_values_of_two_lists(form_input_fields, except_elements_placeholder, "placeholder")

    # fill in form input fields
    random_blog_n = randint(1, 100)
    test_dada = [f'Test{random_blog_n}', f'Something{random_blog_n}', "There are many variations of passages of Lorem "
                                                                      "Ipsum available, but the majority have suffered "
                                                                      "alteration in some form, by injected humour, or "
                                                                      "randomised words which don't look even slightly "
                                                                      "believable.", "quality"]

    fill_input_fields(test_dada, form_input_fields, publish_btn)

    # check url, blog
    time.sleep(5)
    # current_url = driver.current_url
    # print(current_url)
    h1_element = driver.find_element_by_xpath('//div[@class="container"]/h1')
    assert h1_element.text == test_dada[0]
    paragraph = driver.find_element_by_xpath('//div[@class="row article-content"]//p')
    assert paragraph.text == test_dada[2]
    time.sleep(5)
    # check the blog post is included in the global feed list (all pages)
    driver.find_element_by_xpath('//nav/div/ul/li/a[contains(text(), "Home")]').click()
    global_feed_list = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="home-global"]//a[@class="preview-link"]/h1')))

    # create_text_list(global_feed_list, global_posts)
    global_posts = []
    all_pages_link = driver.find_elements_by_xpath('//nav/ul/li[@class="page-item"]/a')
    for link in all_pages_link:
        global_feed_list = WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//div[@class="home-global"]//a[@class="preview-link"]/h1')))
        create_text_list(global_feed_list, global_posts)
        link.click()

    assert test_dada[0] in global_posts
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a[@active-class="active"]').click()  # logout
    time.sleep(3)


# A012_CON_TC13_Meglévő blogbejegyzésem szerkesztése
def test_mod_and_del_blog():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(5)

    # login
    find_elem_and_click('//*[@id="app"]/nav/div/ul/li[@class="nav-item"]/a[@href="#/login"]')
    # log_input_fields = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))
    login_data = []

    with open("login_data.txt", "r") as log_file:
        content = log_file.readlines()
        for i in content:
            login_data.append(i.replace("\n", ""))

    time.sleep(3)
    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')))
    pwd = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')))
    sign_in_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//button[contains(text(),"Sign in")]')))

    email.send_keys(login_data[1])
    pwd.send_keys(login_data[2])
    sign_in_btn.click()

    # driver.find_element_by_xpath('//form/fieldset/input[@placeholder="Email"]').send_keys(login_data[1])
    # driver.find_element_by_xpath('//form/fieldset/input[@placeholder="Password"]').send_keys(login_data[2])
    # find_elem_and_click('//button[contains(text(),"Sign in")]')

    # create new blog
    time.sleep(5)
    find_elem_and_click('//a[@href="#/editor"]')  # editor
    time.sleep(5)
    form_input_fields = driver.find_elements_by_xpath('//form/fieldset//fieldset//input')
    textarea = driver.find_element_by_tag_name('textarea')
    publish_btn = driver.find_element_by_xpath('//form/button')
    form_input_fields.insert(2, textarea)

    # fill in form input fields
    random_blog_n = randint(1, 100)
    test_dada = [f'Fest{random_blog_n}', f'Festival{random_blog_n}', "THE BIGGEST DANCEHALL PARTY IN NYC, D.C. ATL IS "
                                                                     "HEADED BACK TO LOS ANGELES", "quality"]

    fill_input_fields(test_dada, form_input_fields, publish_btn)

    time.sleep(3)
    h1_element = driver.find_element_by_xpath('//div[@class="container"]/h1')
    assert h1_element.text == test_dada[0]
    time.sleep(5)
    # edit
    edit_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/a')
    edit_btn.click()
    mod_test_dada = ["test modify", " Sun", "Sunny. Yesterday my life was fill the rain.", "sun"]
    time.sleep(5)

    def clear_fields(xp, my_list):
        driver.find_element_by_xpath(xp).clear()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xp)))
        driver.find_element_by_xpath(xp).send_keys(my_list)

    clear_fields('//fieldset[1]/input', mod_test_dada[0])
    clear_fields('//fieldset[2]/input', mod_test_dada[1])
    clear_fields('//fieldset/fieldset[3]/textarea', mod_test_dada[2])
    driver.find_element_by_xpath('//fieldset[4]/div/div/ul/li[1]/div[2]/i[2]').click()
    driver.find_element_by_xpath('//fieldset/fieldset[4]/div/div/ul/li/input[@class="ti-new-tag-input ti-valid"]')\
        .send_keys(mod_test_dada[3])
    driver.find_element_by_xpath('//form/button').click()
    time.sleep(5)

    # # check blog
    assert h1_element.text == mod_test_dada[0]

    # A012_CON_TC14_Meglévő blogbejegyzésem törlése
    time.sleep(3)
    driver.find_element_by_xpath('//div/span/button[@class="btn btn-outline-danger btn-sm"]').click()  # delete btn
    # check delete blog in global feeds
    time.sleep(3)
    driver.find_element_by_xpath('//nav/div/ul/li/a[contains(text(), "Home")]').click()
    global_feed_list = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="home-global"]//a[@class="preview-link"]/h1')))
    global_posts = []
    all_pages_link = driver.find_elements_by_xpath('//nav/ul/li[@class="page-item"]/a')
    for link in all_pages_link:
        global_feed_list = WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//div[@class="home-global"]//a[@class="preview-link"]/h1')))
        create_text_list(global_feed_list, global_posts)
        link.click()

    time.sleep(5)
    assert not mod_test_dada[0] in global_posts

    # check delete blog in your feeds
    driver.find_element_by_xpath('//div[@class="feed-toggle"]/ul/li[1]/a[contains(text(), "Your Feed")]').click()
    your_posts = []
    your_feed_list = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="home-my-feed"]//a[@class="preview-link"]/h1')))
    all_pages_link = driver.find_elements_by_xpath('//nav/ul/li[@class="page-item"]/a')

    for _ in all_pages_link:
        your_feed_list = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//div[@class="home-my-feed"]//a[@class="preview-link"]/h1')))
        create_text_list(your_feed_list, your_posts)
        _.click()

    time.sleep(5)
    assert not mod_test_dada[0] in your_posts

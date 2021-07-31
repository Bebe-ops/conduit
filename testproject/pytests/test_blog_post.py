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


def locator(xp):
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xp)))
    return element


def locators(xp):
    element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, xp)))
    return element


def fill_input_fields_and_send(my_list, field_list, btn):
    for _ in range(len(my_list)):
        field_list[_].send_keys(my_list[_])
    btn.click()


def compare_two_lists(real_list, expected_list, attr):
    for _ in range(len(real_list)):
        assert real_list[_].get_attribute(attr) == expected_list[_]


def create_text_list(real_list, new_list):
    for _ in real_list:
        new_list.append(_.text)


# locators
form_input_fields_xp = '//form/fieldset//fieldset//input'
textarea_xp = '//fieldset/textarea'
publish_btn_xp = '//form/button'
home_link_xp = '//nav/div/ul/li/a[contains(text(), "Home")]'
global_feed_list_xp = '//div[@class="home-global"]//a[@class="preview-link"]/h1'
all_pages_link_xp = '//nav/ul/li[@class="page-item"]/a'
logout_xp = '//*[@id="app"]/nav/div/ul/li[5]/a[@active-class="active"]'

# ------------------------------------------------------------------------------------------


# A011_CON_TC10_Új blogbejegyzés (minden mező kitöltése)
def test_new_blog():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # successful registration
    registration_xp = '//li[@class="nav-item"]/a[@href="#/register"]'
    reg_input_fields_xp = '//input'
    sign_up_btn_xp = '//button[contains(text(),"Sign up")]'
    notice_btn_xp = '//div[@class="swal-button-container"]/button'
    new_article_xp = '//a[@href="#/editor"]'
    random_user = f"Hose{randint(1, 100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]

    locator(registration_xp).click()
    locators(reg_input_fields_xp)

    # registration and save login data in file
    login_data = []
    for _ in range(len(reg_input_data)):
        locators(reg_input_fields_xp)[_].send_keys(reg_input_data[_])
    for _ in locators(reg_input_fields_xp)[1:]:
        login_data.append(_.get_attribute("value"))
    with open("login_data.txt", "w") as login_file:  # write data_list in file
        for item in login_data:
            login_file.write("%s\n" % item)
    locator(sign_up_btn_xp).click()

    time.sleep(2)
    locator(notice_btn_xp).click()

    # create new blog_post
    expect_elements_placeholder = ["Article Title", "What's this article about?", "Write your article (in markdown)",
                                   "Enter tags"]
    random_blog_n = randint(1, 100)
    blog_test_data = [f'Summer{random_blog_n}', f'Sun{random_blog_n}',
                      "There are many variations of passages of Lorem Ipsum available, but the majority have suffered "
                      "alteration in some form, by injected humour, or randomised words which don't look even slightly "
                      "believable.", "quality"]
    blog_title_xp = '//div[@class="container"]/h1'
    blog_paragraph_xp = '//div[@class="row article-content"]//p'

    with open('blog_data.txt', "w") as blog_file:  # write data_list in file
        for _ in blog_test_data:
            blog_file.write("%s\n" % _)

    locator(new_article_xp).click()
    form_input_fields = locators(form_input_fields_xp)
    form_input_fields.insert(2, locator(textarea_xp))  # make full form fields

    # check placeholders
    compare_two_lists(form_input_fields, expect_elements_placeholder, "placeholder")

    # fill in form input fields
    fill_input_fields_and_send(blog_test_data, form_input_fields, locator(publish_btn_xp))

    # check url, blog
    time.sleep(2)
    expected_blog = blog_test_data[0]
    expected_url = f'http://localhost:1667/#/articles/{expected_blog.lower()}'
    assert driver.current_url == expected_url

    assert locator(blog_title_xp).text == blog_test_data[0]
    assert locator(blog_paragraph_xp).text == blog_test_data[2]

    # check the blog post is included in the global feed list (all pages)
    locator(home_link_xp).click()
    locators(global_feed_list_xp)

    # create_text_list(from global_feed_list to global_posts)
    global_posts = []
    all_pages_link = locators(all_pages_link_xp)
    for page in all_pages_link:
        global_feed_list = locators(global_feed_list_xp)
        create_text_list(global_feed_list, global_posts)
        page.click()

    assert blog_test_data[0] in global_posts
    locator(logout_xp).click()
    time.sleep(3)


# A012_CON_TC13_Meglévő blogbejegyzésem szerkesztése
def test_mod_and_del_blog():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # login
    login_xp = '//*[@id="app"]/nav/div/ul/li[@class="nav-item"]/a[@href="#/login"]'
    log_input_fields_xp = '//input'
    sign_in_btn_xp = '//button[contains(text(),"Sign in")]'

    locator(login_xp).click()

    # Collect previous login_data
    login_data = []
    with open("login_data.txt", "r") as log_file:
        content = log_file.readlines()
        for i in content:
            login_data.append(i.replace("\n", ""))

    # login
    log_input_fields = locators(log_input_fields_xp)
    fill_input_fields_and_send(login_data, log_input_fields, locator(sign_in_btn_xp))
    time.sleep(3)

    # modified blog
    my_articles_title_xp = '//div[@class="article-preview"]//a//h1'
    nav_bar_user_xp = '//*[@id="app"]/nav/div/ul/li[4]/a'

    blog_data = []
    with open("blog_data.txt", "r") as blog_file:  # Collect previous blog_data
        content = blog_file.readlines()
        for _ in content:
            blog_data.append(_.replace("\n", ""))

    user_name = locator(nav_bar_user_xp)
    user_id_nav_xp = f'//nav//li/a[contains(text(), "{user_name.text}")]'
    locator(user_id_nav_xp).click()
    time.sleep(5)

    # find_my_blog_title
    my_blog_title = locator(f'{my_articles_title_xp}[contains(text(), "{blog_data[0]}")]')
    my_blog_title.click()

    # edit blog
    article_page_h1_xp = '//div[@class="container"]/h1'
    edit_btn_xp = '//div//span//a//span[contains(text(), "Edit Article")]'
    mod_test_data = ["test modify", " Sun", "Sunny. Yesterday my life was fill the rain.", "sun"]
    locator(edit_btn_xp).click()

    form_input_fields = locators(form_input_fields_xp)
    form_input_fields.insert(2, locator(textarea_xp))  # make full form fields

    for _ in range(len(mod_test_data)):
        form_input_fields[_].clear()
        if form_input_fields[_].get_attribute("placeholder") == "Enter tags":
            locator('//div//i[@class="ti-icon-close"]').click()
        form_input_fields[_].send_keys(mod_test_data[_])
    locator(publish_btn_xp).click()

    # check blog
    assert locator(article_page_h1_xp).text == mod_test_data[0]

# A012_CON_TC14_Meglévő blogbejegyzésem törlése
    time.sleep(3)
    delete_btn_xp = '//div/span/button[@class="btn btn-outline-danger btn-sm"]'
    your_feed_xp = '//div[@class="feed-toggle"]/ul/li[1]/a[contains(text(), "Your Feed")]'
    your_feed_list_xp = '//div[@class="home-my-feed"]//a[@class="preview-link"]/h1'

    locator(delete_btn_xp).click()

    # check delete blog in global feeds
    time.sleep(3)
    locator(home_link_xp).click()
    locators(global_feed_list_xp)

    # create_text_list(from global_feed_list to global_posts)
    global_posts = []
    all_pages_link = locators(all_pages_link_xp)
    for page in all_pages_link:
        global_feed_list = locators(global_feed_list_xp)
        create_text_list(global_feed_list, global_posts)
        page.click()

    time.sleep(5)
    assert not mod_test_data[0] in global_posts

    # check delete blog in your feeds
    locator(your_feed_xp).click()
    your_posts = []
    all_pages_link = locators(all_pages_link_xp)

    for _ in all_pages_link:
        your_feed_list = locators(your_feed_list_xp)
        create_text_list(your_feed_list, your_posts)
        _.click()

    time.sleep(5)
    assert not mod_test_data[0] in your_posts
    locator(logout_xp).click()

import csv
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


def find_and_clear_by_xp(xp):
    element = driver.find_element_by_xpath(xp)
    element.clear()
    return element


# locators
# registration locators
registration_xp = '//li[@class="nav-item"]/a[@href="#/register"]'
reg_input_fields_xp = '//input'
sign_up_btn_xp = '//button[contains(text(),"Sign up")]'
notice_btn_xp = '//div[@class="swal-button-container"]/button'
# blog create locators
new_article_xp = '//a[@href="#/editor"]'
article_title_xp = '//input[@placeholder="Article Title"]'
article_desc_xp = '//fieldset[2]/input'
text_area_xp = '//textarea'
tag_xp = '//input[@placeholder="Enter tags"]'
publish_btn_xp = '//form/button'
home_link_xp = '//nav/div/ul/li/a[contains(text(), "Home")]'


# A014_CON_TC15_Címkék használata & TC16_Címke feed oldal
def test_tags():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(2)

    # successful registration
    random_user = f"Buddie{randint(1, 100)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]

    locator(registration_xp).click()
    fill_input_fields_and_send(reg_input_data, locators(reg_input_fields_xp), locator(sign_up_btn_xp))
    locator(notice_btn_xp).click()
    time.sleep(2)

    # create new blog_post
    locator(new_article_xp).click()
    time.sleep(3)

    # create some blog post (read data_list in file and fill blog input fields & write tags in list)
    tags_list = []
    with open("new_blogs.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="|")
        next(reader)
        for row in reader:
            locator(new_article_xp).click()
            time.sleep(3)
            find_and_clear_by_xp(article_title_xp).send_keys(row[0])
            find_and_clear_by_xp(article_desc_xp).send_keys(row[1])
            find_and_clear_by_xp(text_area_xp).send_keys(row[2])
            find_and_clear_by_xp(tag_xp).send_keys(f'{row[3]},{row[4]}')
            tags_list.append(row[3])
            tags_list.append(row[4])
            locator(publish_btn_xp).click()
            time.sleep(3)

    # check tags in My Articles
    blog_summer_tags_xp = '//a[@href="#/articles/summer"]//div[@class="tag-list"]/a'
    blog_spring_tags_xp = '//a[@href="#/articles/spring"]//div[@class="tag-list"]/a'
    blog_winter_tags_xp = '//a[@href="#/articles/winter"]//div[@class="tag-list"]/a'
    blog_autumn_tags_xp = '//a[@href="#/articles/autumn"]//div[@class="tag-list"]/a'

    user_name_in_nav = reg_input_data[0]
    user_name_nav_xp = f'//nav//li/a[contains(text(), "{user_name_in_nav}")]'
    locator(user_name_nav_xp).click()

    # tags of blogs
    def create_blog_tags_list(elements, tag_list):
        for _ in elements:
            tag_list.append(_.text)

    # summer blog
    blog_summer_tags = locators(blog_summer_tags_xp)
    blog_summer_tags_text = []
    create_blog_tags_list(blog_summer_tags, blog_summer_tags_text)
    assert blog_summer_tags_text == tags_list[:2]

    # spring blog
    blog_spring_tags = locators(blog_spring_tags_xp)
    blog_spring_tags_text = []
    create_blog_tags_list(blog_spring_tags, blog_spring_tags_text)
    assert blog_spring_tags_text == tags_list[2:4]

    # winter blog
    blog_winter_tags = locators(blog_winter_tags_xp)
    blog_winter_tags_text = []
    create_blog_tags_list(blog_winter_tags, blog_winter_tags_text)
    assert blog_winter_tags_text == tags_list[4:6]

    # autumn blog
    blog_autumn_tags = locators(blog_autumn_tags_xp)
    blog_autumn_tags_text = []
    create_blog_tags_list(blog_autumn_tags, blog_autumn_tags_text)
    assert blog_autumn_tags_text == tags_list[6:]

    # check test tags in popular tags
    all_tags_xp = '//div[@class="sidebar"]/div[@class="tag-list"]/a'
    common_tag_xp = '//div[@class="sidebar"]/div[@class="tag-list"]/a[contains(text(), "season")]'
    locator(home_link_xp).click()

    popular_tags = []
    for _ in locators(all_tags_xp):
        popular_tags.append(_.text)

    for _ in tags_list:
        assert _ in popular_tags

    # check common tag
    common_tag_blogs_xp = '//div[@class="home-tag"]//h1'
    common_tag_in_blogs_xp = '//div[@class="home-tag"]//a[contains(text(), "season")]'
    driver.refresh()
    locator(common_tag_xp).click()
    assert len(locators(common_tag_blogs_xp)) == len(locators(common_tag_in_blogs_xp))
    expected_url = 'http://localhost:1667/#/tag/season'
    assert driver.current_url == expected_url

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mód


# A001, CON_TC01_Home page megjelenése login nélkül
def test_homepage_without_login():
    url = "http://localhost:1667"
    driver.get(url)
    time.sleep(5)

    def displayed_and_enabled(xp):
        element = driver.find_element_by_xpath(xp)
        assert element.is_displayed()
        assert element.is_enabled()

    # Check the Global feed
    displayed_and_enabled('//div[@class="feed-toggle"]/ul/li')

    # Check that the Popular tags list is visible and enabled and that existing tags are included in the list
    popular_tags = driver.find_elements_by_xpath('//div[@class="tag-list"]/a')
    test_tag = 'leo'
    popular_tags_text = []
    for _ in popular_tags:
        assert _.is_displayed()
        assert _.is_enabled()
        popular_tags_text.append(_.text)
    assert test_tag in popular_tags_text

    # Check the navbar  (check that the user is not logged in)
    nav_bar_links = driver.find_elements_by_xpath('//nav//div[@class="container"]/ul/li')
    expected_nav_bar_elements = ['Home', 'Sign in', 'Sign up']
    nav_bar_links_text = []
    for i in nav_bar_links:
        nav_bar_links_text.append(i.text)
    assert expected_nav_bar_elements == nav_bar_links_text

    # Check the navbar elements
    displayed_and_enabled('//li[@class="nav-item"]/a[@href="#/login"]')
    displayed_and_enabled('//li[@class="nav-item"]/a[@href="#/register"]')
    displayed_and_enabled('//li[@class="nav-item"]//a[contains(text(), "Home")]')
    driver.close()

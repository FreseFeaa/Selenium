import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




@pytest.mark.parametrize("link_text",["305763", "643051", "003388", "756480", "704777", "376026", "641158", "362417", "641158", "968992", "210864", "586451", "224592", "385461", "809857", "132869", "190051", "986293", "623566", "356349", "385461", "441456"])
def test_find_link_text(browser,link_text):
    url = ("http://suninjuly.github.io/find_link_text")
    browser.get(url)
    browser.find_element(By.LINK_TEXT,link_text).click()

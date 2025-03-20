import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def browser():

    browser = webdriver.Firefox()
    browser.set_window_size(1200, 1200)

    yield browser
    print("\n quit browser")
    browser.quit()

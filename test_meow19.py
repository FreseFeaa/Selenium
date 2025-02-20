import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://selenium1py.pythonanywhere.com/"


def test_guest_see_login_link(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR,"#login_link")

#pytest -s -v --browser_name=firefox test_meow19.py
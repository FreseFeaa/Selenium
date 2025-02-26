import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_find_button_add_cart(browser):
    url = ("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
    browser.get(url)
    buttontext = browser.find_element(By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
    print(buttontext)
    time.sleep(4)
    assert buttontext.is_displayed(), "Нет кнопки("

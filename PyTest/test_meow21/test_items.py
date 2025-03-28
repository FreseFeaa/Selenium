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
    print()
    assert buttontext.is_displayed(), "Нет кнопки("

def test_failing_jira(browser,jira_client):
    url = ("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
    browser.get(url)
    buttontext = browser.find_element(By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
    assert buttontext.text == "Точно не будет", "Тест ожидаемо упал"

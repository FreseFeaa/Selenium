import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


def test_guest_see_login_button(browser):
    url = ("https://ogorodnik.by/")
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_button()

def test_guest_can_login_in_account(browser):
    url = ("https://ogorodnik.by/")
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_in_account()

    
    




import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_go_to_login_page(browser):
    url = ("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()
    page.go_to_link_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()




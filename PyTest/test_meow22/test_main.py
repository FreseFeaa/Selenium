import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .pages.main_page import MainPage

def test_guest_go_to_login_page(browser):
    url = ("https://selenium1py.pythonanywhere.com")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()



import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage



# Общая большая кт  - Паттерн PageObject
@pytest.mark.all_test
@pytest.mark.main_page
def test_guest_see_login_button(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()

@pytest.mark.all_test
@pytest.mark.main_page
@pytest.mark.login
def test_guest_can_login_in_account(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_in_account()

@pytest.mark.all_test
@pytest.mark.main_page
@pytest.mark.register
def test_guest_can_register_in_new_account(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    page.reg_button_click()
    login_page = LoginPage(browser, browser.current_url)
    login_page.reg_new_account()

@pytest.mark.all_test
@pytest.mark.main_page
@pytest.mark.register
def test_guest_not_can_register_in_old_account(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    page.reg_button_click()
    login_page = LoginPage(browser, browser.current_url)
    login_page.reg_old_account()

@pytest.mark.all_test
@pytest.mark.main_page
@pytest.mark.basket
def test_add_to_basket_direktor_cucumber_f1(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.catalog_search("Огурец Директор F1")
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.product_in_basket("Огурец Директор F1")

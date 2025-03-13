import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


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


def test_guest_can_register_in_new_account(browser):
    url = ("https://ogorodnik.by/")
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    page.reg_button_click()
    login_page = LoginPage(browser, browser.current_url)
    login_page.reg_new_account()


def test_guest_not_can_register_in_old_account(browser):
    url = ("https://ogorodnik.by/")
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    page.reg_button_click()
    login_page = LoginPage(browser, browser.current_url)
    login_page.reg_old_account()

def test_add_to_basket_direktor_cucumber_f1(browser):
    url = ("https://ogorodnik.by/")
    page = BasePage(browser, url)
    page.open()
    page.catalog_search_direktor_cucumberF1()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.add_to_basket_direktor()



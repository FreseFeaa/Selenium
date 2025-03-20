import time
import pytest
from .pages.main_page import MainPage
from .utils.screen import compare_img
from selenium.webdriver.common.by import By

@pytest.mark.main_screen
def test_screen_main_page_is_good(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()
    time.sleep(1)
    browser.save_screenshot("Pytest/test_meow25/sreenshots/test_main_page_img.png")
    assert compare_img("Pytest/test_meow25/sreenshots/base_main_page_img.png", "Pytest/test_meow25/sreenshots/test_main_page_img.png"), "Изображения сайта не совпали"

@pytest.mark.banner_screen
def test_screen_banner_is_good(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()
    time.sleep(1)
    banner = browser.find_element(By.CLASS_NAME, "vc_column-inner.vc_custom_1651571909539")
    banner.screenshot("Pytest/test_meow25/sreenshots/test_banner.png")
    assert compare_img("Pytest/test_meow25/sreenshots/base_banner.png", "Pytest/test_meow25/sreenshots/test_banner.png"), "Изображения баннеров не совпали"

@pytest.mark.full_screen
def test_full_screen(browser):
    url = ("https://ogorodnik.by/")
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_button()
    time.sleep(1)
    browser.save_full_page_screenshot("Pytest/test_meow25/sreenshots/test_full_screen.png")
    assert compare_img("Pytest/test_meow25/sreenshots/base_full_screen.png", "Pytest/test_meow25/sreenshots/test_full_screen.png"), "Изображения полного сайта не совпали"



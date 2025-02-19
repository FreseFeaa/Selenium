import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://selenium1py.pythonanywhere.com/"

@pytest.mark.parametrize("language",["ru","en-gb"])
def test_guest_see_login0(browser, language):
    browser.get(url+language)
    print("тест 0, язык: ", language)
    browser.find_element(By.CSS_SELECTOR,"#login_link")

@pytest.mark.parametrize("language",["ru","en-gb"])
class TestLogin():
    def test_guest_see_login1(self, browser, language):
        browser.get(url+language)
        print("тест 1, язык: ", language)
        browser.find_element(By.CSS_SELECTOR,"#login_link")

    def test_guest_see_login2(self, browser, language):
        browser.get(url+language)
        print("тест 2, язык: ", language)
        browser.find_element(By.CSS_SELECTOR,"#login_link")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n Start browser")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\n Quit browser")
        self.browser.quit()

    def test_guest(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR,"#login_link")

    def test_guest2(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR,".basket-mini .btn-group > a")

class TestMainPage2():

    def setup_method(self):
        print("\n Start browser")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\n Quit browser")
        self.browser.quit()

    def test_guest(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR,"#login_link")

    def test_guest2(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR,".basket-mini .btn-group > a")
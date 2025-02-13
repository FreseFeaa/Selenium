import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


#Этот файл в разработке, я мало че понял, поэтому оно пока чт не работает

url = "https://selenium1py.pythonanywhere.com/"

class TestMainPage1():
    @classmethod
    def setup_class(self):
        print("\n Start browser")
        self.browser = webdriver.Chrome()

    @classmethod
    def setup_class(self):
        print("\n Quit browser")
        self.browser.quit()

    def test_link1(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR,"#login_link")

    def test_link2(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR,".basket-mini .btn-group > a")
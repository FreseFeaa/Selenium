import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self,browser,url,timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    
    def is_element_present(self,how,what):
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False
        
        return True


    def is_not_element_present(self,how,what,timeout=5):
        try:
            WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            return True
        return False
    
    
    def is_disappeared(self,how,what,timeout=5):
        try:
            WebDriverWait(self.browser,timeout,poll_frequency=TimeoutException).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            return True
        return False
    

    def go_to_link_page(self):
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login.click()

    def should_be_login_button(self):
        assert self.is_element_present(*BasePageLocators.ACCOUNT_BUTTON), "Нет кнопки профиля"
    
    def login_button_click(self):
        self.browser.find_element(*BasePageLocators.ACCOUNT_BUTTON).click()

    def reg_button_click(self):
        self.browser.find_element(*BasePageLocators.REG_BUTTON).click()

    def catalog_search_direktor_cucumberF1(self):
        self.browser.find_element(*BasePageLocators.CATALOG_SEARCH).send_keys(*BasePageLocators.DIRECTOR_CUCUMBER_F1) 
    # def open_basket(self):
    #     login = self.browser.find_element(*BasePageLocators.BUTTON_BASKET)
    #     login.click()
            
from string import ascii_lowercase
from random import choices
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import MainPageLocators
from ..config import LoginAccountData
from ..config import RegisterAccountData

class LoginPage(BasePage):
    def login_in_account(self):
        self.browser.find_element(*MainPageLocators.INPUT_USER_NAME).send_keys(*LoginAccountData.BASE_USERNAME) 
        self.browser.find_element(*MainPageLocators.INPUT_PASSWORD).send_keys(*LoginAccountData.BASE_PASSWORD)  
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        self.browser.find_element(*BasePageLocators.ACCOUNT_BUTTON).click()
        assert self.browser.find_element(*LoginPageLocators.ACCOUNT_TITTLE).text == "Личный кабинет" , "При входе в аккаунт чёт пошло не так"

    def reg_new_account(self):
        random_string = ''.join(choices(ascii_lowercase, k=16)) 

        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_NAME).send_keys(random_string) 
        self.browser.find_element(*LoginPageLocators.REG_NEW_EMAIL).send_keys(random_string + "@gmail.com")  
        self.browser.find_element(*LoginPageLocators.REG_NEW_PASSWORD).send_keys(random_string)  
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()  
        assert self.browser.find_element(*LoginPageLocators.ACCOUNT_TITTLE).text == "Личный кабинет" , "При регистрации нового аккаунт чёт пошло не так"

    def reg_old_account(self):
        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_NAME).send_keys(*LoginAccountData.BASE_USERNAME) 
        self.browser.find_element(*LoginPageLocators.REG_NEW_EMAIL).send_keys(*RegisterAccountData.BASE_USER_EMAIL)  
        self.browser.find_element(*LoginPageLocators.REG_NEW_PASSWORD).send_keys(*LoginAccountData.BASE_PASSWORD)  
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()  
        assert self.browser.find_element(*LoginPageLocators.REG_ERROR_TEXT).text == "Ошибка: Учётная запись под таким адресом электронной почты уже зарегистрирована. Войти.", "При регистрации уже сущ. акка чёт пошло не так"

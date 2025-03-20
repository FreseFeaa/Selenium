from string import ascii_lowercase
from random import choices
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import MainPageLocators
from ..config import LoginAccountData


class LoginPage(BasePage):
    def login_in_account(self):
        self.browser.find_element(*MainPageLocators.INPUT_USER_NAME).send_keys(*LoginAccountData.BASE_USERNAME) 
        self.browser.find_element(*MainPageLocators.INPUT_PASSWORD).send_keys(*LoginAccountData.BASE_PASSWORD)  

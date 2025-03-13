from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def login_in_account(self):
        self.browser.find_element(*LoginPageLocators.INPUT_USER_NAME).send_keys(*LoginPageLocators.BASE_USERNAME) 
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(*LoginPageLocators.BASE_PASSWORD)  
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        self.browser.find_element(*BasePageLocators.ACCOUNT_BUTTON).click()
        assert self.browser.find_element(*LoginPageLocators.ACCOUNT_TITTLE).text == "Личный кабинет" , "При входе в аккаунт чёт пошло не так"

    def reg_new_account(self):
        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_NAME).send_keys(*LoginPageLocators.NEW_USER_NAME) 
        self.browser.find_element(*LoginPageLocators.REG_NEW_EMAIL).send_keys(*LoginPageLocators.NEW_USER_EMAIL)  
        self.browser.find_element(*LoginPageLocators.REG_NEW_PASSWORD).send_keys(*LoginPageLocators.NEW_USER_PASSWORD)  
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()  
        assert self.browser.find_element(*LoginPageLocators.ACCOUNT_TITTLE).text == "Личный кабинет" , "При регистрации нового аккаунт чёт пошло не так"

    def reg_old_account(self):
        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_NAME).send_keys(*LoginPageLocators.BASE_USERNAME) 
        self.browser.find_element(*LoginPageLocators.REG_NEW_EMAIL).send_keys(*LoginPageLocators.NEW_USER_EMAIL)  
        self.browser.find_element(*LoginPageLocators.REG_NEW_PASSWORD).send_keys(*LoginPageLocators.BASE_PASSWORD)  
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()  
        assert self.browser.find_element(*LoginPageLocators.REG_ERROR_TEXT).text == "Ошибка: Учётная запись под таким адресом электронной почты уже зарегистрирована. Войти.", "При регистрации уже сущ. акка чёт пошло не так"

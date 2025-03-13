from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def add_to_basket_direktor(self):
        self.browser.find_element(*BasketPageLocators.ADD_TO_CART_BUTTON).click()
        self.browser.find_element(*BasketPageLocators.BASKET_BUTTON).click()  
        assert self.browser.find_element(*BasketPageLocators.CUCUMBER_IN_BASKET).text == BasePageLocators.DIRECTOR_CUCUMBER_F1
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Нет сообщения о пустой корзине"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "В корзине есть что-то"
            
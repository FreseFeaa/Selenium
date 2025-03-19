from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def product_in_basket(self,product):
        assert self.browser.find_element(By.LINK_TEXT,product).text == product

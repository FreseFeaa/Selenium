from selenium.webdriver.common.by import By

class BasePageLocators():
    ACCOUNT_BUTTON = (By.CLASS_NAME,"wd-tools-icon")
    
class MainPageLocators():
    pass

# class BasketPageLocators():
#     BASKET_EMPTY_MESSAGE = (By.ID, "content_inner")
#     BASKET_ITEMS = (By.CLASS_NAME, "basket-items")

class LoginPageLocators():
    INPUT_USER_NAME = (By.ID,"username") 
    BASE_USERNAME = "FreseFea"
    INPUT_PASSWORD = (By.ID,"password") 
    BASE_PASSWORD = "test123"
    LOGIN_BUTTON = (By.NAME,"login")
    ACCOUNT_TITTLE = (By.CSS_SELECTOR,"#h1")
    #aaaa = (aaaa)
    #aaaa = (aaaa)
    #aaaa = (aaaa)
    #aaaa = (aaaa)


class PageObjectLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADD_TO_CART_TEXT = (By.CSS_SELECTOR, ".alertinner strong")
    ADD_TO_CART_TEXT_FULL = (By.CLASS_NAME, "alertinner")
    NAME_BOOK = (By.CSS_SELECTOR, "h1")
    PRICE_CART = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_BOOK = (By.CLASS_NAME, "price_color")
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form") 
    REGISTOR_FORM = (By.ID, "register_form") 

class PageObjectLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADD_TO_CART_TEXT = (By.CSS_SELECTOR, ".alertinner strong")
    ADD_TO_CART_TEXT_FULL = (By.CLASS_NAME, "alertinner")
    NAME_BOOK = (By.CSS_SELECTOR, "h1")
    PRICE_CART = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_BOOK = (By.CLASS_NAME, "price_color")
from selenium.webdriver.common.by import By

class BasePageLocators():
    ACCOUNT_BUTTON = (By.CLASS_NAME,"wd-tools-icon")
    CATALOG_SEARCH = (By.CSS_SELECTOR,"[title='Поиск по каталогу']")

class MainPageLocators():
    REG_BUTTON = (By.LINK_TEXT, "СОЗДАТЬ АККАУНТ")
    INPUT_USER_NAME = (By.ID,"username") 
    INPUT_PASSWORD = (By.ID,"password") 
    LOGIN_BUTTON = (By.NAME,"login")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.NAME,"add-to-cart")
    BASKET_BUTTON = (By.LINK_TEXT,"ПРОСМОТР КОРЗИНЫ")


class LoginPageLocators():
    ACCOUNT_TITTLE = (By.CLASS_NAME,"entry-title.title")
    REG_NEW_USER_NAME = (By.ID, "reg_username")
    REG_NEW_EMAIL = (By.ID, "reg_email")
    REG_NEW_PASSWORD = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.CLASS_NAME, "woocommerce-Button.button.wp-element-button")
    REG_ERROR_TEXT = (By.CLASS_NAME, "woocommerce-notices-wrapper")


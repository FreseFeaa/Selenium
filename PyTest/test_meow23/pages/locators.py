from selenium.webdriver.common.by import By

class BasePageLocators():
    ACCOUNT_BUTTON = (By.CLASS_NAME,"wd-tools-icon")
    REG_BUTTON = (By.LINK_TEXT, "СОЗДАТЬ АККАУНТ")
    CATALOG_SEARCH = (By.CSS_SELECTOR,"[title='Поиск по каталогу']")
    DIRECTOR_CUCUMBER_F1 = "Огурец Директор F1"

class BasketPageLocators():
    ADD_TO_CART_BUTTON = (By.NAME,"add-to-cart")
    BASKET_BUTTON = (By.LINK_TEXT,"ПРОСМОТР КОРЗИНЫ")
    CUCUMBER_IN_BASKET = (By.LINK_TEXT,"Огурец Директор F1")

class LoginPageLocators():
    INPUT_USER_NAME = (By.ID,"username") 
    BASE_USERNAME = "FreseFea"
    INPUT_PASSWORD = (By.ID,"password") 
    BASE_PASSWORD = "test123"
    LOGIN_BUTTON = (By.NAME,"login")
    ACCOUNT_TITTLE = (By.CLASS_NAME,"entry-title.title")

    REG_NEW_USER_NAME = (By.ID, "reg_username")
    NEW_USER_NAME = "testovich12"
    REG_NEW_EMAIL = (By.ID, "reg_email")
    NEW_USER_EMAIL = "testovich12@gmail.com"
    REG_NEW_PASSWORD = (By.ID, "reg_password")
    NEW_USER_PASSWORD = ("test123")
    REGISTER_BUTTON = (By.CLASS_NAME, "woocommerce-Button.button.wp-element-button")
    REG_ERROR_TEXT = (By.CLASS_NAME, "woocommerce-notices-wrapper")


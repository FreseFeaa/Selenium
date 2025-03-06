from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
# class MainPage(BasePage):
    # def go_to_link_page(self):
    #     login = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login.click()
    #     # return LoginPage(browser = self.browser,url = self.browser.current_url)

#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Нет ссылки на страницу авторизации"
            
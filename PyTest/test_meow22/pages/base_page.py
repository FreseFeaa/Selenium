import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self,browser,url,timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    
    def is_element_present(self,how,what):
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False
        
        return True


    def is_not_element_present(self,how,what,timeout=5):
        try:
            WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            return True
        return False
    
    
    def is_disappeared(self,how,what,timeout=5):
        try:
            WebDriverWait(self.browser,timeout,poll_frequency=TimeoutException).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            return True
        return False
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(f"{answer}")
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_link_page(self):
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login.click()
        # return LoginPage(browser = self.browser,url = self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Нет ссылки на страницу авторизации"

    def open_basket(self):
        login = self.browser.find_element(*BasePageLocators.BUTTON_BASKET)
        login.click()
            
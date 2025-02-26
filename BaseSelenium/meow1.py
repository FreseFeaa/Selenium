from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    inputFirstName = browser.find_element(By.NAME,"first_name")
    inputFirstName.send_keys("Test")

    inputLastName = browser.find_element(By.NAME, "last_name")
    inputLastName.send_keys("Testovich")

    inputCity = browser.find_element(By.NAME, "firstname")
    inputCity.send_keys("Testovburg")

    inputCountry = browser.find_element(By.ID, "country")
    inputCountry.send_keys("Russia")

    buttonElement = browser.find_element(By.ID, "submit_button")
    buttonElement.click()

    time.sleep(5)

finally:
    browser.quit()



# print(browser.find_element(By.ID, "text"))
# print(browser.find_element(By.CSS_SELECTOR, "#text"))
# print(browser.find_element(By.XPATH, "//input"))
# print(browser.find_element(By.NAME, "text"))
# print(browser.find_element(By.TAG_NAME, "input"))
# print(browser.find_element(By.CLASS_NAME, "search3__input"))
# print(browser.find_element(By.LINK_TEXT, "Войти"))
# print(browser.find_element(By.PARTIAL_LINK_TEXT, "Во"))

# for a in browser.find_elements(By.TAG_NAME, "a"):
#     print(a)


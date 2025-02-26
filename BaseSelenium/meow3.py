from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration1.html")

    required_elements = browser.find_elements(By.CSS_SELECTOR, '[required]')



    a = 0
    for element in required_elements:
        # print(element.get_attribute("class"))
        match a:
            case 0:
                element.send_keys("Test")
                a+= 1
            case 1:
                element.send_keys("Testovich")
                a+= 1
            case 2:
                element.send_keys("Testom@gmail.com")
                a+= 1
            case _:
                print('Errooor')

    buttonElement = browser.find_element(By.CLASS_NAME, "btn.btn-default")
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


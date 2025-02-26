import math
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

import time


try:
    browser = webdriver.Chrome()
    browser.get("http://workerbntu.github.io/tests/alert_accept.html")

    ButtonStart =browser.find_element(By.TAG_NAME,"button")
    ButtonStart.click()

    browser.switch_to.alert.accept()
    

    mathnumb = browser.find_element(By.ID, "input_value").text
    print(mathnumb)
    answerMath = browser.find_element(By.ID,"answer")  
    answerMath.send_keys(math.log(math.fabs(12 * math.sin(int(mathnumb)))))  
    itogButton =browser.find_element(By.TAG_NAME,"button")
    itogButton.click()

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
# browser.execute_script("document.title='AXAXAXA';alert(document.title)")
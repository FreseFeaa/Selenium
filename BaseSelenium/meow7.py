import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://workerbntu.github.io/tests/wait1.html")


    browser.find_element(By.TAG_NAME,"button").click()
    assert browser.find_element(By.ID,"verify_message").text == "Verification was successful!"

    time.sleep(10)

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
# browser.get_cookies()
# browser.add_cookie({"id":"1"})
# browser.delete_all_cookies()   

import math
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

import time

browser = webdriver.Chrome()
try:

    browser.implicitly_wait(5)
    browser.get("https://ogorodnik.by/")

    
    #Регистрация нового аккаунта
    print("Регистрация нового аккаунта", end='')
    browser.find_element(By.CLASS_NAME,"wd-tools-icon").click()
    browser.find_element(By.LINK_TEXT, "СОЗДАТЬ АККАУНТ").click()  
    browser.find_element(By.ID, "reg_username").send_keys("testovich11") 
    browser.find_element(By.ID, "reg_email").send_keys("testovich11@gmail.com")  
    browser.find_element(By.ID, "reg_password").send_keys("test123")  
    browser.find_element(By.CLASS_NAME, "woocommerce-Button.button.wp-element-button").click()  
    assert browser.find_element(By.CLASS_NAME,"entry-title.title").text == "Личный кабинет"
    print(" - успешно")
    
    #Выход из аккаунта
    print("Выход из аккаунта", end='')
    browser.delete_all_cookies()
    browser.get("https://ogorodnik.by/")
    browser.find_element(By.CLASS_NAME,"wd-tools-icon").click() 
    assert browser.find_element(By.LINK_TEXT, "СОЗДАТЬ АККАУНТ").text == "СОЗДАТЬ АККАУНТ"
    print(" - успешно")

    #Регистрация существующего аккаунта
    print("Регистрация существующего аккаунта", end='')
    browser.find_element(By.LINK_TEXT, "СОЗДАТЬ АККАУНТ").click()  
    browser.find_element(By.ID, "reg_username").send_keys("test") 
    browser.find_element(By.ID, "reg_email").send_keys("test@gmail.com")  
    browser.find_element(By.ID, "reg_password").send_keys("test123")  
    browser.find_element(By.CLASS_NAME, "woocommerce-Button.button.wp-element-button").click() 
    assert browser.find_element(By.CLASS_NAME, "woocommerce-notices-wrapper").text == "Ошибка: Учётная запись под таким адресом электронной почты уже зарегистрирована. Войти."
    print(" - успешно")

    #Вход в аккаунт
    print("Вход в аккаунт", end='')
    browser.find_element(By.CLASS_NAME,"wd-tools-icon").click()
    browser.find_element(By.ID,"username").send_keys("FreseFea") 
    browser.find_element(By.ID,"password").send_keys("test123")  
    browser.find_element(By.NAME,"login").click()
    browser.find_element(By.CLASS_NAME,"wd-tools-icon").click()
    assert browser.find_element(By.CLASS_NAME,"entry-title.title").text == "Личный кабинет"
    print(" - успешно")


    #Добавление товара в корзину и проверка наличия его там
    print("Добавление товара в корзину и проверка наличия его там", end='') 
    browser.find_element(By.CSS_SELECTOR,"[title='Поиск по каталогу']").send_keys("Огурец Директор F1") 
    browser.find_element(By.NAME,"add-to-cart").click()
    browser.find_element(By.LINK_TEXT,"ПРОСМОТР КОРЗИНЫ").click()  
    assert browser.find_element(By.LINK_TEXT,"Огурец Директор F1").text == "Огурец Директор F1" 
    print(" - успешно")


    time.sleep(5)
finally:
    browser.quit()




# print(browser.find_element(By.ID, "text"))
# print(browser.find_element(By.CSS_SELECTOR, "#text"))
# browser.find_element(By.CSS_SELECTOR, "[data-product_id='7746']")
# print(browser.find_element(By.XPATH, "//input"))
# print(browser.find_element(By.NAME, "text"))
# print(browser.find_element(By.TAG_NAME, "input"))
# print(browser.find_element(By.CLASS_NAME, "search3__input"))
# print(browser.find_element(By.LINK_TEXT, "Войти"))
# print(browser.find_element(By.PARTIAL_LINK_TEXT, "Во"))
# browser.execute_script("document.title='AXAXAXA';alert(document.title)")
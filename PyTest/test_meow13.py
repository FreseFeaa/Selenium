import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("https://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException): #Ищем тут ошибку не найденного элемента (with всё закроет красиво)
            browser.find_element(By.CSS_SELECTOR,"button.btn") #Ищем кнопку, если она найдеться код идёт дальше
            pytest.fail('Такой кнопки быть не должно') #Из-за того что кнопка нашлась, то выполняеться эта строчка (pytest провален)
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("https://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException): #Ищем тут ошибку не найденного элемента (with всё закроет красиво)
            browser.find_element(By.CSS_SELECTOR,"no_such_button.btn")#Ищем кнопку, если она найдеться не найдеться, то будет нужная нам ошибка и with всё закроет
            pytest.fail('Такой кнопки быть не должно') #Из-за того что кнопка не нашлась, то  эта строчка  не выполняеться(pytest пройден)
    finally:
        browser.quit()
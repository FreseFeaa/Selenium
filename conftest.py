import pytest
from selenium import webdriver

#Файл для фикстур

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    print("\n start browser")
    yield browser
    #Код после теста
    print("\n quit browser")
    browser.quit()

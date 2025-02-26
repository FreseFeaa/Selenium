import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://selenium1py.pythonanywhere.com/"

@pytest.fixture  #(scope="class") - Можно задать область видимости
def browser():
    browser = webdriver.Chrome()
    print("\n start browser")
    yield browser
    #Код после теста
    print("\n quit browser")
    browser.quit()

@pytest.fixture(autouse=True)
def prepairData():
    print("\n Подготовка данных")

@pytest.mark.full_class 
class TestMainPage():

    @pytest.mark.win10
    @pytest.mark.smoke 
    def test_guest(self, browser):
        print("\n start test1")
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR,"#login_link")
        print("\n end test1")

    @pytest.mark.regression 
    @pytest.mark.skip
    def test_guest2(self, browser):
        print("\n start test2")
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR,".basket-mini .btn-group > a")
        print("\n end test2")

    @pytest.mark.xfail(reason="Комментарий к заранее правильно заваленому тесту")
    def test_guest3(self, browser):
        print("\n start test3")
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR,".basketKFC")
        print("\n end test3")
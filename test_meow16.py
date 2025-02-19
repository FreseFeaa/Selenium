import pytest

url = "https://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class") # Вначале класса и в конце после всех методов
def prepair_class():
    print("\n Начало класса")
    yield
    print("\n Конец класса")
    #2 Принта будет

@pytest.fixture # Только там где она явно указывается 
def prepair_import():
    print("На меня явно указали (ШОК)")
    #1  Принт будет

@pytest.fixture(autouse=True) # Для каждого теста, без явного указания
def prepair_smile():
    print("\n Начало каждого метода")
    #2  Принта будет

class TestMainPage():

    def test_guest(self, prepair_class, prepair_import):
        print("первый тест")
    def test_guest2(self, prepair_class):
        print("второй тест")
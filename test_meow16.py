import pytest

url = "https://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class") # Вначале класса и в конце после всех методов
def prepair_class():
    print("\n Начало класс")
    yield
    print("\n Конец класс")
    #2 Принта будет

@pytest.fixture # Только там где она явно указывается 
def prepair_import():
    print(":)","\n")
    #1  Принт будет

@pytest.fixture(autouse=True) # Для каждого метода в классе
def prepair_smile():
    print("\n :-p")
    #2  Принта будет

class TestMainPage():

    def test_guest(self, prepair_class, prepair_import):
        print("первый тест")
    def test_guest2(self, prepair_class):
        print("второй тест")
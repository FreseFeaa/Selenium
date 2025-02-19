# Поиск элемента:
# browser.find_element(By.ID, "text")
# browser.find_element(By.CSS_SELECTOR, "#text")
# browser.find_element(By.CSS_SELECTOR, "[data-product_id='7746']")
# browser.find_element(By.XPATH, "//input")
# browser.find_element(By.NAME, "text")
# browser.find_element(By.TAG_NAME, "input")
# browser.find_element(By.CLASS_NAME, "search3__input")
# browser.find_element(By.LINK_TEXT, "Войти")
# browser.find_element(By.PARTIAL_LINK_TEXT, "Во")

# Взаимодействие с элементами
# buttonElement = browser.find_element(By.TAG_NAME, "button").click()
# inputFirstName = browser.find_element(By.NAME,"first_name").send_keys("Test")

# Исполнение скриптов
# browser.execute_script("document.title='AXAXAXA';alert(document.title)")
# browser.execute_script("return arguments[0].scrollIntoView(true);",selectButton)

# Работа с окнами
# browser.switch_to.window(browser.window_handles[1])

# Базовый assert
# assert browser.find_element(By.CLASS_NAME,"CoolClass").text == "Всё ок"

# Работа с Cookie
# browser.get_cookies()
# browser.add_cookie({"id":"1"})
# browser.delete_all_cookies()

# Неявное ожидание
# browser.implicitly_wait(5)


#Работа с unittest
# import unittest
# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-50),50,"Должно быть положительное") 
        
#     def test_abs2(self):
#         self.assertEqual(abs(-50),-50,"Должно быть положительное") 
# if __name__ == "__main__":
#     unittest.main()
#     print('Готово')


#.venv в Vscode (Виртуальное окружение, для установки в него зависимостей)
#Справа снизу версия питона
#Createe Vitrual Environment
#Venv
#Python Версия MicrosoftStore
#Открыть не powershell, а cmd = Возможно надо будет перезагрузить VSC

#pip freeze > requirements.txt
#Сохраняет все зависимости в requirements.txt, Нужно делать в виртуальном окружении (Глобально может подтянуть вообще всё)
#pip install -r requirements.txt
#Скачать все зависимости из requirements.txt


#Pytest ищет файлы test_*.py или *_test.py
# Внутри этих файлов ищет:
# Функции test*()  (Вне классов)
# Методы test*()   (Внутри классов Test* и без метода __init__)

#pytest -s -v -m "smoke and win10" test_meow15.py
# -s : C принтами
# -v : Подробная информация
# -m : Конкретный тест через marker 


#Маркеровка
#@pytest.mark.smoke - создание маркера на тест
# + его нужно обьявить в файле pytest.ini
# Пример файла
# [pytest]
# markers =
#     smoke: Это тесты на каждый коммит
#pytest -m "smoke and win10"/"not win10"/"smoke or win10" test_meow15.py (Можно еще указать файл, иначе он будет по всей директории искать)
#Маркеры с доп. свойствами:
# @pytest.mark.skip - скипнуть тест
# @pytest.mark.xfail - заранее обусловленно-заваленный тест
# (reason="Комментарий гойда для теста")

# Параметры
# @pytest.mark.parametrize("language",["ru","en-gb"]) - можно передать какие-то значения для теста 
# @pytest.mark.parametrize("language",[("ru","en-gb"),("ru","en-gb")]) - или целком картежи

# Декораторы
# @classmethod                          # Декоратор
# def setup_class(self):                # Фикстура: Произойдет перед всеми методами класса
#     print("\n Start browser")
#     self.browser = webdriver.Chrome()

# @classmethod                          # Декоратор
# def teardown_class(self):             # Фикстура: Произойдет после всех методов класса
#     print("\n Quit browser")
#     self.browser.quit()


# def setup_method(self):               # Произойдет перед КАЖДЫМ методом класса
#     print("\n Start browser")
#     self.browser = webdriver.Chrome()

# def teardown_method(self):            # Произойдет после КАЖДОГО метода класса
#     print("\n Quit browser")
#     self.browser.quit()


# Фикстуры и декараторы pytest
# @pytest.fixture(scope="class")        # Вначале класса и в конце после всех методов
# def prepair_class():
#     print("\n Начало класса")
#     yield # Финализатор (Как return, но когда над ним все действия выполнятся - код после него будет выполнен)
#     print("\n Конец класса")

# @pytest.fixture                       # Только там где она явно указывается 
# def prepair_import():
#     print("На меня явно указали")

# @pytest.fixture(autouse=True)         # Для каждого теста, без явного указания
# def prepair_smile():
#     print("\n Начало каждого метода")


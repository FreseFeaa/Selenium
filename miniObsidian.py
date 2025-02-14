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
#freeze - (TODO изучить)

#Pytest ищет файлы test_*.py или *_test.py
# Внутри этих файлов ищет:
# Функции test*()  (Вне классов)
# Методы test*()   (Внутри классов Test* и без метода __init__)


#pytest -s -v -m "smoke and win10" test_meow15.py
# -s : C принтами
# -v : Подробная информация
# -m : Конкретный тест через marker 
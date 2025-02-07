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
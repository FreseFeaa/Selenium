import os
from datetime import datetime
import pytest
from jira import JIRA
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


load_dotenv(override=True) # Подгружаем значения из .env

API_TOKEN = os.getenv("API_TOKEN_SIGMA")  # Присваемываем эти значения
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")

bag_screenshot = "Test_JIRA/test_meow26/bag_screenshot.png"

def pytest_addoption(parser):  # Делаем доп. возможности управлять тестами при запуске с консоли
    parser.addoption("--languages",action="store",default="ru",help="Выберите язык")
    parser.addoption("--jira",action="store_true", help="Включить интеграцию с jira")


@pytest.fixture(scope="session") # Запускаем фикстуру на всю сессию
def jira_client(request):
    if request.config.getoption("jira"):     # Еслм у нас в консоли при запуске была --jira :
        jira = JIRA( server=JIRA_SERVER, basic_auth=(JIRA_USERNAME,API_TOKEN))  # Логинемся с помощью этих данных и получаем обьект с которым можно работать
        return jira

@pytest.fixture  # Фикстура для запуска браузера
def browser(request):
    language = request.config.getoption("languages")  # Если есть какой-то язык - кидаем его в настройки
    options =Options()
    options.add_experimental_option("prefs",{"intl.accept_languages":language})
    browser = webdriver.Chrome(options=options)
    yield browser  # Возвращаем обьект нашего браузера
    print("\n quit browser")
    browser.quit()  # После отработки фикстуры закрываем браузер

@pytest.hookimpl(hookwrapper=True) # декоратор - при фазах теста 
def pytest_runtest_makereport(item,call):  # Получаем 2 аргумента  
    outcome = yield  # Здесь неявно присваеваем call в outcome
    report = outcome.get_result() #Получаем информацию о нашем проекте
    print(report) # <TestReport 'Test_JIRA/test_meow26/test_items.py::test_failing_jira' when='setup' outcome='passed'> Вот так она выглядит, мы получаем такой принт после каждого этапа теста (Запуск, сам тест, закрытие (Примерн так))

    if report.when == "call" and hasattr(report,"wasxfail") and report.outcome == "passed": # Если тест должен был провалиться, но он почему-то прошел - мы выводим это сообщение
        print("Тест с меткой xfail - почему-то прошёл")

    if report.when == "call" and report.outcome == "failed": # Если тест не прошёл:
        if "browser" in item.funcargs: # Смотрим есть ли у нас там обьект браузер
            browser = item.funcargs["browser"]  # Обращаемся конкретно к нему (Через items)
            browser.save_screenshot(bag_screenshot)  # И теперь с помощью браузера делаем скриншот нашей страницы
        if "jira_client" in item.funcargs: # Теперь ищем обьект jira_client
            jira = item.funcargs["jira_client"] # Cохраняем все аргументы jira
            if jira:   # Если jira не пустая то:
                issue_type = jira.issue_types()  # Смотрим какие вообще типы есть у нее
                print("_"*40+"SIGMA PRINT"+"_"*40)
                print(jira.projects()) # [<JIRA Project: key='SIGMA', name='SigmaTest', id='10001'>, <JIRA Project: key='CPG', name='Test', id='10000'>] - информация о проектах в jira
                print(jira.issue_types()) # Получаем информацию о типах в наших проектах
                bug_type = issue_type[5]  # Выбираем тип задачи (Баг)
                jira_issue = {
                    "project": {"key": "SIGMA"},
                    "summary":f"{item.name}",
                    "description": f"Ошибка: {report.longreprtext}\n\n Дата: {datetime.now()}",
                    "issuetype": {"id":bug_type.id}
                    }   # заполняем информацию о баге
                new_issue = jira.create_issue(fields=jira_issue)  # Создаем задачу по нашим полям

                jira.add_attachment(new_issue.key,bag_screenshot)  # Прикрепляем к нашей задаче файл (В нашем случае скриншот проваленного теста, который сделали до этого)
                

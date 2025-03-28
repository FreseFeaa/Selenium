import os
from datetime import datetime
import pytest
from jira import JIRA
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


load_dotenv(override=True)

API_TOKEN = os.getenv("API_TOKEN", "ЗАПИХНИТЕ СЮДА КЛЮЧ")
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")

def pytest_addoption(parser):
    parser.addoption("--languages",action="store",default="ru",help="Выберите язык")
    parser.addoption("--jira",action="store_true", help="Включить интеграцию с jira")

@pytest.fixture(scope="session")
def jira_client(request):
    if request.config.getoption("jira"):
        jira = JIRA( server=JIRA_SERVER, basic_auth=(JIRA_USERNAME,API_TOKEN))
        return jira

@pytest.fixture
def browser(request):
    language = request.config.getoption("languages")
    options =Options()
    options.add_experimental_option("prefs",{"intl.accept_languages":language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n quit browser")
    browser.quit()

@pytest.hookimpl(hookwrapper=True) # декоратор - при фазах теста 
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    print(report)

    if report.when == "call" and hasattr(report,"wasxfail") and report.outcome == "passed":
        print("Тест с меткой xfail - почему-то прошёл")

    if report.when == "call" and report.outcome == "failed":
        if "browser" in item.funcargs:
            browser = item.funcargs["browser"]
            browser.save_screenshot("PyTest/test_meow21/test.png")
        if "jira_client" in item.funcargs:
            jira = item.funcargs["jira_client"]
            if jira:
                issue_type = jira.issue_types()
                print(jira.projects())
                bug_type = issue_type[4]
                jira_issue = {
                    "project": {"key": "SIGMA"},
                    "summary":f"{item.name}",
                    "description": f"Ошибка: {report.longreprtext}\n\n Дата: {datetime.now()}",
                    "issuetype": {"id":bug_type.id}
                    }
                new_issue = jira.create_issue(fields=jira_issue)

                jira.add_attachment(new_issue.key,"PyTest/test_meow21/test.png")
                

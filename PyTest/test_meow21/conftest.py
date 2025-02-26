import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--languages",action="store",default="ru",help="Выберите язык")

@pytest.fixture
def browser(request):
    language = request.config.getoption("languages")
    options =Options()
    options.add_experimental_option("prefs",{"intl.accept_languages":language})

    browser = webdriver.Chrome(options=options)


    yield browser
    print("\n quit browser")
    browser.quit()

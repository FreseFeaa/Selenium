import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
url = "https://google.com"

options =Options()
options.add_experimental_option("prefs",{"intl.accept_languages":"de"})

browser = webdriver.Chrome(options=options)

browser.get(url)
time.sleep(5)

browser.quit()
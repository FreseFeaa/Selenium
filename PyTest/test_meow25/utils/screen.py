import time
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.common.by import By

def screen_main_page():
    try:
        url = ("https://ogorodnik.by/")
        browser = webdriver.Firefox()
        browser.get(url)
        browser.set_window_size(1200, 1200)
        time.sleep(1)
        browser.save_screenshot("Pytest/test_meow25/sreenshots/base_main_page_img.png")
    finally:
        browser.quit()

def screen_banner():
    try:
        url = ("https://ogorodnik.by/")
        browser = webdriver.Firefox()
        browser.get(url)
        browser.set_window_size(1200, 1200)
        time.sleep(1)
        banner = browser.find_element(By.CLASS_NAME, "vc_column-inner.vc_custom_1651571909539")
        banner.screenshot("Pytest/test_meow25/sreenshots/base_banner.png")
    finally:
        browser.quit()
    
def screen_full_website():
    try:
        url = ("https://ogorodnik.by/")
        browser = webdriver.Firefox()
        browser.get(url)
        browser.set_window_size(1200, 1200)
        time.sleep(1)
        browser.save_full_page_screenshot("Pytest/test_meow25/sreenshots/base_full_screen.png")

    finally:
        browser.quit()
def compare_img(img1_path,img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    diff = ImageChops.difference(img1,img2)
    print(diff)
    
    if diff.getbbox() == None:
        return True
    else:
        return False
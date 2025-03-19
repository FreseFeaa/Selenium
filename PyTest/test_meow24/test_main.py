import pytest
from .utils.screen import compare_img
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.skip
def test_img_browser(browser):
    
    browser.get(url)
    browser.save_screenshot("Pytest/test_meow24/sreenshots/img1.png")
    assert compare_img("Pytest/test_meow24/sreenshots/goodimg.png", "Pytest/test_meow24/sreenshots/img1.png"), "Изображения не совпали"
    
def test_img_element(browser):
    browser.get(url)
    u1 = browser.find_element(By.ID,"product_gallery")
    u1.screenshot("Pytest/test_meow24/sreenshots/u1.png")



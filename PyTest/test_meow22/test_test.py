import pytest
from .pages.product_page import PageObject

@pytest.mark.xfail
def test_test1(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = PageObject(browser, url) 
    page.open()
    page.add_cart()
    page.shoud_is_not_result_message()

def test_test2(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = PageObject(browser, url) 
    page.open()
    page.shoud_is_not_result_message()    

@pytest.mark.xfail
def test_test3(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = PageObject(browser, url) 
    page.open()
    page.add_cart()
    page.shoud_is_desapperared()
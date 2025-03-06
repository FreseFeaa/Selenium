import pytest
from .pages.product_page import PageObject
from .pages.basket_page import BasketPage

@pytest.mark.skip
@pytest.mark.parametrize("url",["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,url):
    # url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, url) 
    page.open()
    page.add_cart()
    page.solve_quiz_and_get_code()
    page.shoud_product_add_to_cart()
    page.shoud_product_price_and_cart()

def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = PageObject(browser, url) 
    page.open()
    page.should_be_login_link()

def test_guest_should_go_login_page_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = PageObject(browser, url) 
    page.open()
    page.go_to_link_page()


def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    url = ("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page = PageObject(browser, url) 
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.is_basket_empty_message()
    
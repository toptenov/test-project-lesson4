from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time # Можно удалить
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    book_name = page.define_book_name()
    book_price = page.define_book_price()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_correct_book_name(book_name)
    page.should_be_price_message()
    page.should_be_correct_book_price(book_price)

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    book_name = page.define_book_name()
    book_price = page.define_book_price()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"])

def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])

def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    book_name = page.define_book_name()
    book_price = page.define_book_price()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_link()
    log_page = LoginPage(browser, browser.current_url)
    log_page.should_be_login_page()

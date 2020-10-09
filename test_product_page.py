from pages.product_page import ProductPage
import time # Можно удалить
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

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
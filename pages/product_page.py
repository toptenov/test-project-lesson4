from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_in_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_BOOK_NAME), "Success message is not presented"

    def should_be_correct_book_name(self):
        data = (*ProductPageLocators.ADDED_BOOK_NAME, "The shellcoder's handbook")
        assert self.is_text_in_element_correct(*data), "Book name is not correct"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_IN_SUCCESS_MESSAGE), "Book price is not presented"

    def should_be_correct_book_price(self):
        data = (*ProductPageLocators.BOOK_PRICE_IN_SUCCESS_MESSAGE, "£9.99")
        assert self.is_text_in_element_correct(*data), "Book price is not correct"

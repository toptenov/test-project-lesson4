from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def __init__(self, *args, **kwargs):
		super(BasketPage, self).__init__(*args, **kwargs)

	def should_not_be_products_on_basket_page(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_BLOCK), "Basket is not empty"

	def should_be_text_of_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.TEXT_OF_EMPTY_BASKET), "There is no text of empty basket"

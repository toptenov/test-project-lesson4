from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn.btn-lg.btn-primary")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
	ADDED_BOOK_NAME = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in div.alertinner strong")
	BOOK_PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in div.alertinner strong")
	BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
	BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
	SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_ITEMS_BLOCK = (By.CSS_SELECTOR, ".basket-items")
	TEXT_OF_EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")

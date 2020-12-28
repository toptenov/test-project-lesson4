import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	browser = webdriver.Chrome(options=options)
	print("\nstart chrome browser for test..")
	yield browser
	print("\nquit browser..")
	browser.quit()
	
def pytest_configure(config):
    config.addinivalue_line("markers", "user_adds_product: marks test to run only on mark 'user_adds_product'")
    config.addinivalue_line("markers", "login_guest: marks test to run only on mark 'login_guest'")
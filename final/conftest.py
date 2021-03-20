import time

import pytest
from selenium import webdriver

from final.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default="en-GB",
                     help='Choose user language: "ru", "en-GB", "es", "fr"')


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request, language):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f"Browser {browser_name} still is not implemented")

    yield browser
    browser.quit()


@pytest.fixture()
def register_new_user(browser):
    login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"

    def _register_new_user():
        email = str(time.time()) + "@test.org"
        password = "test_user_password"
        page = LoginPage(browser, login_page_url)
        page.open()
        page.register_new_user(email, password)
        return email, password

    return _register_new_user

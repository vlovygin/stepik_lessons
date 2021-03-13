import pytest
from selenium import webdriver
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default="en-GB",
                     help='Choose user language: "ru", "en-GB", "es", "fr"')


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request, user_language):
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f"Browser {browser_name} still is not implemented")

    yield browser
    browser.quit()

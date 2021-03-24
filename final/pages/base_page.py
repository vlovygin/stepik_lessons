from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from final.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def input(self, how, what, value):
        element = self.browser.find_element(how, what)
        element.click()
        element.clear()
        element.send_keys(value)

    def click(self, how, what):
        element = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((how, what)))
        element.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_success_messages(self):
        elements = self.browser.find_elements(*BasePageLocators.SUCCESS_MESSAGE)
        return [element.text for element in elements]

    def logout(self):
        self.click(*BasePageLocators.LOGOUT_BUTTON)

    def go_to_profile_page(self):
        self.click(*BasePageLocators.ACCOUNT_BUTTON)

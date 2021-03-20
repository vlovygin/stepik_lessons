import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from final.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
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

    def click(self, how, what, timeout=4):
        element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
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
    def get_error_messages(self):
        elements = self.browser.find_elements(*BasePageLocators.SUCCESS_MESSAGE)
        return [element.text for element in elements]

    def should_be_registered_user_message(self):
        assert "Thanks for registering!" in self.get_success_messages(), \
            "Success registration message is not presented"

    def logout(self):
        self.click(*BasePageLocators.LOGOUT_BUTTON)

    def should_be_login_user_message(self):
        assert "Welcome back" in self.get_success_messages(), "Success login message is not presented"

    # def go_to_account_page(self):
    #     self.click(*BasePage.)

    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                  " probably unauthorised user"

#

#
#     def get_element_text(self, how, what):
#         element = self.browser.find_element(how, what)
#         return element.text
#
#     def get_elements_text(self, how, what):
#         elements = self.browser.find_elements(how, what)
#         return [element.text for element in elements]
#
#     def is_not_element_present(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return True
#         return False
#
#     def is_disappeared(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout, 1, TimeoutException). \
#                 until_not(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return False
#         return True
#
#     def go_to_login_page(self):
#         link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
#         link.click()
#
#     def go_to_basket_page(self):
#         link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
#         link.click()
#
#     def should_be_login_link(self):
#         assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
#

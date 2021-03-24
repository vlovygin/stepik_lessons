from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        super().__init__(browser, url)

    def register_new_user(self, email, password):
        self.input(*LoginPageLocators.REGISTER_FORM_EMAIL, email)
        self.input(*LoginPageLocators.REGISTER_FORM_PASSWORD, password)
        self.input(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD, password)
        self.click(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)

    def login(self, email, password):
        self.input(*LoginPageLocators.LOGIN_FORM_EMAIL, email)
        self.input(*LoginPageLocators.LOGIN_FORM_PASSWORD, password)
        self.click(*LoginPageLocators.LOGIN_FORM_SUBMIT_BUTTON)

    def get_error_messages(self):
        elements = self.browser.find_elements(*LoginPageLocators.ERROR_MESSAGE)
        return [element.text for element in elements]

    def should_be_login_error_message(self):
        excepted_error = "Please enter a correct username and password. Note that both fields may be case-sensitive."
        assert excepted_error in self.get_error_messages(), f"Login error message '{excepted_error}' is not presented"

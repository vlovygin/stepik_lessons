from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

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

    def should_be_error_login_message(self):
        assert "Please enter a correct username and password. Note that both fields may be case-sensitive." in \
               self.get_error_messages(), "Login error message is not presented"


#     def should_be_login_page(self):
#         self.should_be_login_url()
#         self.should_be_login_form()
#         self.should_be_register_form()
#
#     def should_be_login_url(self):
#         current_url = self.browser.current_url
#         assert "login" in current_url, "Browser url should contains 'login'"
#
#     def should_be_login_form(self):
#         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
#
#     def should_be_register_form(self):
#         assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"



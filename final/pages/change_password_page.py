from final.pages.base_page import BasePage
from final.pages.locators import ChangePasswordPageLocators


class ChangePasswordPage(BasePage):
    def __init__(self, browser):
        url = "http://selenium1py.pythonanywhere.com/accounts/profile/change-password/"
        super().__init__(browser, url)

    def change_password(self, old_password, new_password):
        self.input(*ChangePasswordPageLocators.OLD_PASSWORD_INPUT, old_password)
        self.input(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT, new_password)
        self.input(*ChangePasswordPageLocators.NEW_PASSWORD_CONFIRM_INPUT, new_password)
        self.click(*ChangePasswordPageLocators.SAVE_BTN)

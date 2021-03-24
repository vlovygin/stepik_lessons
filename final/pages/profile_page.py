from .base_page import BasePage
from .locators import ProfilePageLocators, DeleteProfilePageLocators, EditProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, browser):
        url = "http://selenium1py.pythonanywhere.com/accounts/profile/"
        super().__init__(browser, url)

    def go_to_edit_profile(self):
        self.click(*ProfilePageLocators.EDIT_PROFILE_BTN)

    def go_to_change_password(self):
        self.click(*ProfilePageLocators.CHANGE_PASSWORD_BTN)

    def go_to_delete_profile(self):
        self.click(*ProfilePageLocators.DELETE_PROFILE_BTN)

    def should_be_profile_updated_message(self):
        excepted_message = "Profile updated"
        assert excepted_message in self.get_success_messages(), \
            f"Profile updated message '{excepted_message}' is not presented"

    def should_be_password_updated_message(self):
        excepted_message = "Password updated"
        assert excepted_message in self.get_success_messages(), \
            f"Password updated message '{excepted_message}' is not presented"

    def check_profile_name(self, first_name, last_name):
        excepted_profile_name = " ".join(filter(None, [first_name, last_name]))
        profile_name_element = self.browser.find_element(*ProfilePageLocators.PROFILE_NAME)
        profile_name = profile_name_element.text
        assert excepted_profile_name == profile_name, \
            f"Excepted profile name: {excepted_profile_name}, actual: {profile_name}"


class EditProfilePage(BasePage):
    def __init__(self, browser):
        url = "http://selenium1py.pythonanywhere.com/accounts/profile/edit"
        super().__init__(browser, url)

    def edit_name(self, first_name, last_name):
        self.input(*EditProfilePageLocators.FIRST_NAME_INPUT, first_name)
        self.input(*EditProfilePageLocators.LAST_NAME_INPUT, last_name)
        self.click(*EditProfilePageLocators.SAVE_PROFILE_BTN)

    def edit_email(self, email):
        self.input(*EditProfilePageLocators.EMAIL_INPUT, email)
        self.click(*EditProfilePageLocators.SAVE_PROFILE_BTN)

    def check_danger_alert(self):
        excepted_alert = "Oops! We found some errors - please check the error messages below and try again"
        alert = self.browser.find_element(*EditProfilePageLocators.DANGER_MESSAGE)
        assert excepted_alert == alert.text, f"Danger alert '{excepted_alert}' is not presented"

    def check_email_form_error(self):
        excepted_error = "A user with this email address already exists"
        error = self.browser.find_element(*EditProfilePageLocators.EMAIL_FORM_ERROR)
        assert excepted_error == error.text, f"Email form error '{excepted_error}' is not presented"


class DeleteProfilePage(BasePage):
    def __init__(self, browser):
        url = "http://selenium1py.pythonanywhere.com/accounts/profile/delete/"
        super().__init__(browser, url)

    def confirm_delete_profile(self, password):
        self.input(*DeleteProfilePageLocators.PASSWORD_INPUT, password)
        self.click(*DeleteProfilePageLocators.DELETE_PROFILE_BTN)

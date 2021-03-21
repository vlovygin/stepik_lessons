from .base_page import BasePage
from .locators import ProfilePageLocators, DeleteProfilePageLocators, EditProfilePageLocators


class ProfilePage(BasePage):

    def go_to_edit_profile(self):
        self.click(*ProfilePageLocators.EDIT_PROFILE_BTN)

    def go_to_delete_profile(self):
        self.click(*ProfilePageLocators.DELETE_PROFILE_BTN)

    def should_be_profile_updated_message(self):
        assert "Profile updated" in self.get_success_messages(), "Profile updated message is not presented"

    def check_profile_name(self, first_name, last_name):
        excepted_profile_name = " ".join(filter(None, [first_name, last_name]))
        profile_name_element = self.browser.find_element(*ProfilePageLocators.PROFILE_NAME)
        profile_name = profile_name_element.text
        assert excepted_profile_name == profile_name, \
            f"Excepted profile name: {excepted_profile_name}, actual: {profile_name}"


class EditProfilePage(BasePage):
    def edit_name(self, first_name, last_name):
        self.input(*EditProfilePageLocators.FIRST_NAME_INPUT, first_name)
        self.input(*EditProfilePageLocators.LAST_NAME_INPUT, last_name)
        self.click(*EditProfilePageLocators.SAVE_PROFILE_BTN)


class DeleteProfilePage(BasePage):
    def confirm_delete_profile(self, password):
        self.input(*DeleteProfilePageLocators.PASSWORD_INPUT, password)
        self.click(*DeleteProfilePageLocators.DELETE_PROFILE_BTN)

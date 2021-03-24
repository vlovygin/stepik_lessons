import time

import pytest

from final.pages.change_password_page import ChangePasswordPage
from final.pages.login_page import LoginPage
from final.pages.main_page import MainPage
from final.pages.profile_page import ProfilePage, EditProfilePage, DeleteProfilePage


@pytest.mark.personal_tests
class TestProfilePage:

    @pytest.fixture(scope="function", autouse=True)
    def open_profile_page_of_existing_user(self, browser, exists_user):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(exists_user.email, exists_user.password)
        login_page.go_to_profile_page()

    @pytest.mark.parametrize("first_name, last_name", [
        ("edited_first_name", "edited_last_name"),
        ("edited_first_name", ""),
        ("", "edited_last_name")])
    def test_user_can_edit_profile_name(self, browser, first_name, last_name):
        # Arrange
        profile_page = ProfilePage(browser)

        # Act
        profile_page.go_to_edit_profile()
        edit_profile_page = EditProfilePage(browser)
        edit_profile_page.edit_name(first_name, last_name)

        # Assert
        profile_page = ProfilePage(browser)
        profile_page.should_be_profile_updated_message()
        profile_page.check_profile_name(first_name, last_name)

    @pytest.mark.negative_test
    def test_user_cant_change_email_to_already_exists(self, browser, exists_user2):
        # Arrange
        profile_page = ProfilePage(browser)

        # Act
        profile_page.go_to_edit_profile()
        edit_profile_page = EditProfilePage(browser)
        edit_profile_page.edit_email(exists_user2.email)

        # Assert
        edit_profile_page.check_danger_alert()
        edit_profile_page.check_email_form_error()

    def test_user_can_change_password(self, browser, exists_user):
        # Arrange
        profile_page = ProfilePage(browser)

        # Act
        profile_page.go_to_change_password()
        change_password_page = ChangePasswordPage(browser)
        change_password_page.change_password(exists_user.password, exists_user.password)

        # Assert
        profile_page = ProfilePage(browser)
        profile_page.should_be_password_updated_message()


@pytest.mark.personal_tests
class TestProfileDelete:

    def test_user_can_delete_profile(self, browser, register_new_user):
        # Arrange
        user = register_new_user()
        profile_page = ProfilePage(browser)
        profile_page.open()

        # Act
        profile_page.go_to_delete_profile()
        delete_profile_page = DeleteProfilePage(browser)
        delete_profile_page.confirm_delete_profile(user.password)

        # Assert
        main_page = MainPage(browser)
        main_page.should_be_deleted_profile_message()

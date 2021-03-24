import pytest

from final.pages.login_page import LoginPage
from final.pages.main_page import MainPage


class TestLoginPage:

    def test_registration_new_user(self, browser, register_new_user):
        # Arrange
        login_page = LoginPage(browser)
        login_page.open()

        # Act
        register_new_user()

        # Assert
        main_page = MainPage(browser)
        main_page.should_be_registered_user_message()

    @pytest.mark.personal_tests
    def test_auth_by_exists_user(self, browser, exists_user):
        # Arrange
        login_page = LoginPage(browser)
        login_page.open()

        # Act
        login_page.login(exists_user.email, exists_user.password)

        # Assert
        main_page = MainPage(browser)
        main_page.should_be_login_user_message()

    @pytest.mark.negative_test
    @pytest.mark.personal_tests
    def test_auth_with_incorrect_password(self, browser, exists_user):
        # Arrange
        exists_user.password += "_incorrect"
        login_page = LoginPage(browser)
        login_page.open()

        # Act
        login_page.login(exists_user.email, exists_user.password)

        # Assert
        login_page.should_be_login_error_message()

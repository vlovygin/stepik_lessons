import pytest

from final.pages.login_page import LoginPage
from final.pages.main_page import MainPage

main_page_url = "http://selenium1py.pythonanywhere.com/"
login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestLoginPage:

    @pytest.mark.personal_tests
    def test_registration_new_user(self, browser, register_new_user):
        # Arrange
        page = LoginPage(browser, login_page_url)
        page.open()

        # Act
        register_new_user()

        # Assert
        page.should_be_registered_user_message()

    @pytest.mark.personal_tests
    def test_auth_by_exists_user(self, browser, register_new_user):
        # Arrange
        email, password = register_new_user()
        page = MainPage(browser, main_page_url)
        page.logout()

        # Act
        page = LoginPage(browser, login_page_url)
        page.open()
        page.login(email, password)

        # Assert
        page.should_be_login_user_message()

    @pytest.mark.personal_tests
    # @pytest.mark.xfail
    def test_auth_by_not_exists_user(self, browser, register_new_user):
        # Arrange
        email, password = "user@mail.ru", "incorrect_password"

        # Act
        page = LoginPage(browser, login_page_url)
        page.open()
        page.login(email, password)

        # Assert
        page.should_be_error_login_message()

import pytest

from final.pages.login_page import LoginPage
from final.pages.main_page import MainPage

main_page_url = "http://selenium1py.pythonanywhere.com/"
login_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.personal_tests
class TestLoginPage:

    def test_registration_new_user(self, browser, register_new_user):
        # Arrange
        login_page = LoginPage(browser, login_page_url)
        login_page.open()

        # Act
        register_new_user()

        # Assert
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_registered_user_message()

    def test_auth_by_exists_user(self, browser, register_new_user):
        # Arrange
        email, password = register_new_user()
        main_page = MainPage(browser, main_page_url)
        main_page.logout()

        # Act
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        login_page.login(email, password)

        # Assert
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_login_user_message()

    @pytest.mark.negative_test
    def test_auth_with_incorrect_password(self, browser, register_new_user):
        # Arrange
        email, password = "user@mail.ru", "incorrect_password"

        # Act
        login_page = LoginPage(browser, login_page_url)
        login_page.open()
        login_page.login(email, password)

        # Assert
        login_page.should_be_login_error_message()

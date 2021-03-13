from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

main_page_link = "http://selenium1py.pythonanywhere.com/"
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, main_page_link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, main_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, main_page_link)
        page.open()

        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.check_basket_is_empty()
        basket_page.check_empty_basket_message()


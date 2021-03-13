import time
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()

        # Act
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.check_basket_product_name_message(product_name)
        page.check_basket_total_price_message(product_price)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)
        page.open()

        # Act
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)

        # Assert
        page.should_be_login_url()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)
        page.open()

        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.check_basket_is_empty()
        basket_page.check_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "test_user_password"

        page = LoginPage(browser, login_page_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, product_page_link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()

        # Act
        page.add_product_to_basket()

        # Arrange
        page.check_basket_product_name_message(product_name)
        page.check_basket_total_price_message(product_price)

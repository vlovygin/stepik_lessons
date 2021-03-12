from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET, timeout=1), \
            "Basket should be empty"

    def check_empty_basket_message(self):
        msg = "Your basket is empty."
        assert msg in self.get_element_text(*BasketPageLocators.BASKET_MESSAGE), \
            f"Empty basket should contain message '{msg}'"

# from .base_page import BasePage
# from .locators import ProductPageLocators
#
#
# class ProductPage(BasePage):
#     def add_product_to_basket(self):
#         self.click(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
#
#     def get_product_name(self):
#         return self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
#
#     def get_product_price(self):
#         return self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
#
#     def check_success_alert_message(self, message):
#         messages = self.get_elements_text(*ProductPageLocators.SUCCESS_MESSAGE)
#         assert message in messages, f"Success message '{message}' is not presented"
#
#     def check_info_alert_message(self, message):
#         messages = self.get_elements_text(*ProductPageLocators.INFO_MESSAGE)
#         assert message in messages, f"Info message '{message}' is not presented"
#
#     def check_basket_product_name_message(self, product_name):
#         self.check_success_alert_message(f"{product_name} has been added to your basket.")
#
#     def check_basket_total_price_message(self, product_price):
#         self.check_info_alert_message(f"Your basket total is now {product_price}")
#
#     def should_not_be_success_message(self):
#         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#            "Success message is presented, but should not be"
#
#     def should_disappeared_success_message(self):
#         assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
#            "Success message is appeared, but should disappeared"

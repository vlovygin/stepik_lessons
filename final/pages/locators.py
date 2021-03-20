from selenium.webdriver.common.by import By


class BasePageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    # USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#login_form #id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#login_form #id_login-password")
    LOGIN_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login_form .btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#login_form .alert-danger")

    #     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    #     REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

#
# class ProductPageLocators:
#     ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn")
#     PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
#     PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
#     SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
#     INFO_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')] //p[not(.//a)]")
#
#
# class BasketPageLocators:
#     BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
#     BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

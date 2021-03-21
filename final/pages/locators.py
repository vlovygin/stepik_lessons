from selenium.webdriver.common.by import By


class BasePageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_link")
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Account")


class LoginPageLocators:
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#login_form #id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#login_form #id_login-password")
    LOGIN_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login_form .btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#login_form .alert-danger")


class ProfilePageLocators:
    EDIT_PROFILE_BTN = (By.LINK_TEXT, "Edit profile")
    DELETE_PROFILE_BTN = (By.CSS_SELECTOR, "#delete_profile")
    PROFILE_NAME = (By.XPATH, "//table //th[text()='Name']//following-sibling::td")


class EditProfilePageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#id_first_name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#id_last_name")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_email")
    SAVE_PROFILE_BTN = (By.CSS_SELECTOR, ".form-group .btn[type='submit']")
    DANGER_MESSAGE = (By.CSS_SELECTOR, "#profile_form .alert-danger")
    EMAIL_FORM_ERROR = (By.CSS_SELECTOR, "#id_email + span")


class DeleteProfilePageLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_password")
    DELETE_PROFILE_BTN = (By.CSS_SELECTOR, ".form-group .btn[type='submit']")

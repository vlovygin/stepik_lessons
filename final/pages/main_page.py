from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        super().__init__(browser, url)

    def should_be_registered_user_message(self):
        excepted_message = "Thanks for registering!"
        assert excepted_message in self.get_success_messages(), \
            f"Success registration message '{excepted_message}' is not presented"

    def should_be_login_user_message(self):
        excepted_message = "Welcome back"
        assert excepted_message in self.get_success_messages(), \
            f"Success login message '{excepted_message}' is not presented"

    def should_be_deleted_profile_message(self):
        excepted_message = "Your profile has now been deleted. Thanks for using the site."
        assert excepted_message in self.get_success_messages(), \
            f"Deleted profile message '{excepted_message}' is not presented"

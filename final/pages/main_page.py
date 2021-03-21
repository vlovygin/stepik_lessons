from .base_page import BasePage


class MainPage(BasePage):

    def should_be_registered_user_message(self):
        assert "Thanks for registering!" in self.get_success_messages(), \
            "Success registration message is not presented"

    def should_be_login_user_message(self):
        assert "Welcome back" in self.get_success_messages(), "Success login message is not presented"

    def should_be_deleted_profile_message(self):
        success_messages = self.get_success_messages()
        assert "Your profile has now been deleted. Thanks for using the site." in success_messages, \
            "Deleted profile message is not presented"

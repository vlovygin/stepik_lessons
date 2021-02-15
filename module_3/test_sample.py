from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru"
user = {"email": "autotest_user@test.ru", "password": "d9eveM0v%g"}

# main page
login_or_authorize_button_locator = "#login_link"
alert_message_locator = "#messages[style*='visible'] div.alert"

# login page
login_form_header_locator = "#login_form h2"
login_email_input_locator = "#id_login-username"
login_password_input_locator = "#id_login-password"
login_submit_button_locator = "button[name='login_submit']"


def test_user_can_be_login():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        login_button = browser.find_element_by_css_selector(login_or_authorize_button_locator)
        login_button.click()

        login_form_header = browser.find_element_by_css_selector(login_form_header_locator)
        assert login_form_header.text == "Войти", "Page should contain login form"

        email_input = browser.find_element_by_css_selector(login_email_input_locator)
        email_input.send_keys(user["email"])
        password_input = browser.find_element_by_css_selector(login_password_input_locator)
        password_input.send_keys(user["password"])
        login_submit_button = browser.find_element_by_css_selector(login_submit_button_locator)
        login_submit_button.click()

        alert_message = browser.find_element_by_css_selector(alert_message_locator)
        assert "Рады видеть вас снова" in alert_message.text, "Page should contain success login alert message"

    finally:
        browser.quit()


test_user_can_be_login()


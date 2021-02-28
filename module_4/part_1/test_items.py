from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

catalog_item_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Locators
add_to_basket_btn_locator = (By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")


def test_item_should_contains_add_to_basket_button(browser, user_language):
    # Arrange
    wait = WebDriverWait(browser, 10)
    button_text = {'ru': 'Добавить в корзину', 'en-GB': 'Add to basket',
                   'es': 'Añadir al carrito', 'fr': 'Ajouter au panier'}
    expected_btn_text = button_text[user_language]

    # Act
    browser.get(catalog_item_link)

    # Assert
    add_to_basket_button = wait.until(EC.visibility_of_element_located(add_to_basket_btn_locator))
    assert add_to_basket_button.text == expected_btn_text, \
        f"Add to basket button should contains text: {expected_btn_text}"

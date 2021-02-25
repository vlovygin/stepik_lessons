from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

catalog_item_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Locators
add_to_basket_button_locator = (By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")


def test_item_should_contains_add_to_basket_button(browser, user_language):
    wait = WebDriverWait(browser, 10)
    # Наименования названия кнопки на разных языках
    button_text = {'ru': 'Добавить в корзину', 'en-GB': 'Add to basket',
                   'es': 'Añadir al carrito', 'fr': 'Ajouter au panier'}
    # Текст кнопки в зависимости от языка
    add_to_basket_button_text = button_text[user_language]

    # Открываем товар по ссылке
    browser.get(catalog_item_link)

    # Страница товара содержит кнопку добавления в корзину с ожидаемым текстом
    add_to_basket_button = wait.until(EC.visibility_of_element_located(add_to_basket_button_locator))
    assert add_to_basket_button.text == add_to_basket_button_text, \
        f"Add to basket button should contains text: {add_to_basket_button_text}"

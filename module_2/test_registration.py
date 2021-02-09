from selenium import webdriver
from sys import argv
import time

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".first_block .first_class > input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector(".first_block .second_class > input")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector(".first_block .third_class> input")
    email.send_keys("ivan_petrov@test.ru")
    phone = browser.find_element_by_css_selector(".second_block .first_class > input")
    phone.send_keys("+79260123456")
    address = browser.find_element_by_css_selector(".second_block .second_class > input")
    address.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

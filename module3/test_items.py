import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary '
                                                               'btn-add-to-basket"]')
    assert add_to_cart_button, "Add to cart button is not found"

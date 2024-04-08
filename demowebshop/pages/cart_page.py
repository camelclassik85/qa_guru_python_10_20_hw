from selene import browser, have
import allure


class CartPage:

    def __init__(self):
        self.product_name = browser.element('.product-name')
        self.checkbox_remove_from_cart = browser.element('[name=removefromcart]')
        self.update_cart = browser.element('[name=updatecart]')
        self.empty_cart_text = browser.element('.order-summary-content')

    def check_presence_item_in_cart(self, item):
        with allure.step(f'Check presence item: {item} in cart'):
            self.product_name.should(have.text(item))

    def clean_cart(self):
        with allure.step('Clean cart'):
            self.checkbox_remove_from_cart.click()
            self.update_cart.click()

    def check_cart_is_empty(self):
        self.empty_cart_text.should(have.text('Your Shopping Cart is empty!'))

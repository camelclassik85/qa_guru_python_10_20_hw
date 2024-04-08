from selene import browser, have
import allure


class MainPage:

    def __init__(self):
        self.account = browser.element('.account')
        self.topcartlink = browser.element('#topcartlink')

    def check_auth_is_success(self, login):
        with allure.step('Check authorization'):
            self.account.should(have.text(login))

    def go_to_cart_page(self):
        with allure.step('Go to cart page'):
            self.topcartlink.click()

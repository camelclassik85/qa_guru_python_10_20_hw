from demowebshop.pages.cart_page import CartPage
from demowebshop.pages.main_page import MainPage


class PageFactory:

    def __init__(self):
        self.main_page = MainPage()
        self.cart_page = CartPage()


pages = PageFactory()

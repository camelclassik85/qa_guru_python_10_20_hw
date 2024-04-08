import allure
from demowebshop.api.add_to_cart import api
from demowebshop.utils.cookie import add_auth_cookie
from demowebshop.pagefactory import pages
from demowebshop.utils.constants import LOGIN, Names, Urls


def test_add_book_to_cart():
    with allure.step('Check add book to cart'):
        api.add_item_to_cart(Urls.BOOK_API_URL)
        add_auth_cookie()
        pages.main_page.check_auth_is_success(LOGIN)
        pages.main_page.go_to_cart_page()
        pages.cart_page.check_presence_item_in_cart(Names.BOOK_NAME)
        pages.cart_page.clean_cart()
        pages.cart_page.check_cart_is_empty()


def test_add_3rd_album_to_cart():
    with allure.step('Check add 3rd album to cart'):
        api.add_item_to_cart(Urls.ALBUM_API_URL)
        add_auth_cookie()
        pages.main_page.check_auth_is_success(LOGIN)
        pages.main_page.go_to_cart_page()
        pages.cart_page.check_presence_item_in_cart(Names.ALBUM_NAME)
        pages.cart_page.clean_cart()
        pages.cart_page.check_cart_is_empty()

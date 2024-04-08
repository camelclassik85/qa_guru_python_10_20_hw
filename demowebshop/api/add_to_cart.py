import allure
from demowebshop.utils.constants import Urls
from demowebshop.utils.cookie import get_auth_cookie
from demowebshop.utils.logger import request_logger


class ApiMethods:

    @staticmethod
    def add_item_to_cart(item):
        with allure.step(f'Add item {item} to cart'):
            request_logger('POST', f'{Urls.DOMAIN_URL}{Urls.API_ADD_PRODUCT_URL}{item}',
                           cookies={'NOPCOMMERCE.AUTH': get_auth_cookie()})


api = ApiMethods()

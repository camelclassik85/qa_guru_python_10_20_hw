from selene import browser
import requests
from demowebshop.utils.constants import Urls, AUTH_DATA


def get_auth_cookie():
    response = requests.post(Urls.DOMAIN_URL + '/login', data=AUTH_DATA, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    return cookie


def add_auth_cookie_to_browser():
    browser.open('/')
    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': get_auth_cookie()})
    browser.open('/')

import os
from dotenv import load_dotenv
from demowebshop.utils.resource import path


dotenv_path = path('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

AUTH_DATA = {
    'Email': LOGIN,
    'Password': PASSWORD
}


class Urls:
    DOMAIN_URL = 'https://demowebshop.tricentis.com'
    API_ADD_PRODUCT_URL = '/addproducttocart/catalog'

    BOOK_API_URL = '/13/1/1'

    ALBUM_API_URL = '/53/1/1'


class Names:
    BOOK_NAME = 'Computing and Internet'
    ALBUM_NAME = '3rd Album'

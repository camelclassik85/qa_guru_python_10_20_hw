import pytest
from selene import browser
from demowebshop.utils.constants import Urls


@pytest.fixture(scope='function', autouse=True)
def set_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = Urls.DOMAIN_URL

    yield browser

    browser.quit()

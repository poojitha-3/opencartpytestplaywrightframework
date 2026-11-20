import pytest

import config
from config import Config
from pages.home_page import Homepage
from pages.login_page import LoginPage
from playwright.sync_api import expect
@pytest.mark.sanity
@pytest.mark.regression
def test_login_page(page):
    homepage = Homepage(page)
    loginpage = LoginPage(page)
    homepage.click_my_account()
    homepage.login_page()
    loginpage.enter_email(Config.invalid_email)
    loginpage.enter_password(Config.invalid_password)
    loginpage.click_login()
    page.wait_for_timeout(2000)
    msg=loginpage.invalid_error()
    expect(msg).to_be_visible(timeout=2000)


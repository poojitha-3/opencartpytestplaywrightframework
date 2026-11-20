import pytest

from pages.home_page import Homepage
from pages.logout_page import LogoutPage
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.my_account import MyAccount
from config import Config

@pytest.mark.regression
def test_logout(page):
    homepage=Homepage(page)
    homepage.click_my_account()
    homepage.login_page()

    loginpage=LoginPage(page)

    loginpage.enter_email(Config.email)
    loginpage.enter_password(Config.password)
    loginpage.click_login()

    my_account_page=MyAccount(page)
    my_account_name=my_account_page.visible_my_account_name()
    expect(my_account_name).to_have_text("My Account")
    page.wait_for_timeout(3000)
    my_account_page.logout()


    log_out=LogoutPage(page)

    msg=log_out.confirm_msg()
    expect(msg).to_have_text("Account Logout")
    page.wait_for_timeout(3000)

    log_out.continue_button()






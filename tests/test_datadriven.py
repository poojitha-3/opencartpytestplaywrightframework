import pytest

from pages.home_page import Homepage
from pages.login_page import LoginPage
from pages.my_account import MyAccount
from utilities.data_reader_utility import data_csv,data_json,data_excel
from config import Config
from playwright.sync_api import expect
csv_data=data_csv("testdata/logindata.csv")
@pytest.mark.datadriven
@pytest.mark.parametrize("testname,email,password,expected",csv_data)
def test_dd(page,testname,email,password,expected):
    homepage = Homepage(page)
    loginpage = LoginPage(page)
    myaccount = MyAccount(page)

    homepage.click_my_account()
    homepage.login_page()

    loginpage.enter_email(email)
    loginpage.enter_password(password)
    loginpage.click_login()
    if expected=="success":
        expect(myaccount.visible_my_account_name()).to_be_visible(timeout=2000)
    else:
        expect(loginpage.invalid_error()).to_be_visible(timeout=2000)





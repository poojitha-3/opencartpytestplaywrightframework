import pytest

from pages import home_page
from pages.home_page import Homepage
from pages.register_page import RegisterPage
from utilities.random_data_utility import RandomDataUtility
from playwright.sync_api import expect
@pytest.mark.sanity
@pytest.mark.regression
def test_register_page(page):
    homepage=Homepage(page)
    registerpage=RegisterPage(page)

    homepage.click_my_account()
    homepage.register_page()

    random=RandomDataUtility()
    registerpage.firstname(random.get_first_name())
    registerpage.lastname(random.get_last_name())
    registerpage.set_email(random.get_email())
    registerpage.telephone(random.get_phone_number())
    password=random.get_password()
    registerpage.set_password(password)
    registerpage.password_confirm(password)
    registerpage.radiocheck()
    registerpage.checkbox()
    registerpage.continue_buton()
    msg=registerpage.confirmation_msg()
    expect(msg).to_have_text("Your Account Has Been Created!")

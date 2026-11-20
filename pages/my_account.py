from playwright.sync_api import Page

from pages.logout_page import LogoutPage


class MyAccount:
    def __init__(self,page:Page):
        self.page = page
        self.click_on_myaccount=self.page.locator("a[title='My Account']")
        self.visible_my_account=self.page.locator("h2:has-text('My Account')")
        self.click_on_logout=self.page.locator("a:nth-child(13)")


    def click_on_myaccount(self):
        self.click_on_myaccount.click()

    def visible_my_account_name(self):
        return self.visible_my_account

    def logout(self):
        self.click_on_logout.click()


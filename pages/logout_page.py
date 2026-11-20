from playwright.sync_api import Page

from pages.home_page import Homepage


class LogoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.click_myaccount=self.page.locator("a[title='My Account']")
        self.click_logout=self.page.locator("li[class='dropdown open'] li:nth-child(5) a:nth-child(1)")
        self.msg_confirmation=self.page.locator("h1:has-text('Account Logout')")
        self.click_continue=self.page.locator(".btn.btn-primary")

    def click_my_account(self):
        try:
            self.click_myaccount.click()
        except Exception as e:
            print(f"error msg while clicking my account: {e}")
            raise

    def logout(self):
        try:
            self.click_logout.click()
        except Exception as e:
            print(f"error msg while clicking logout: {e}")
            raise

    def confirm_msg(self):
        return self.msg_confirmation

    def continue_button(self):
        self.click_continue.click()
        return Homepage(self.page)



from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page):
        self.page = page
        self.email=self.page.locator("#input-email")
        self.password=self.page.locator("#input-password")
        self.login_button=self.page.locator("input[value='Login']")
        self.error_msg=self.page.locator(".alert.alert-danger.alert-dismissible")


    def enter_email(self,email):
        try:
            self.email.fill(email)
        except Exception as e:
            print(f"error while entering email: {e}")
            raise

    def enter_password(self,password):
        try:
            self.password.fill(password)
        except Exception as e:
            print(f"error while entering password: {e}")
            raise

    def click_login(self):
        self.login_button.click()

    def invalid_error(self):
        return self.error_msg




from playwright.sync_api import Page


class RegisterPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_name=self.page.locator("#input-firstname")
        self.last_name=self.page.locator("#input-lastname")
        self.email=self.page.locator("#input-email")
        self.tele_phone=self.page.locator("#input-telephone")
        self.password=self.page.locator("#input-password")
        self.confirm_password=self.page.locator("#input-confirm")
        self.radio_check=self.page.locator("input[value='0']")
        self.check_box=self.page.locator("input[value='1'][name='agree']")
        self.click_continue=self.page.locator("input[value='Continue']")
        self.msg_confirmation=self.page.locator("h1:has-text('Your Account Has Been Created!')")


    def firstname(self,firstname):
        self.first_name.fill(firstname)

    def lastname(self,lastname):
        self.last_name.fill(lastname)

    def set_email(self,email):
        self.email.fill(email)

    def telephone(self,telephone):
        self.tele_phone.fill(telephone)

    def set_password(self,password):
        self.password.fill(password)

    def password_confirm(self,confirm_password):
        self.confirm_password.fill(confirm_password)

    def radiocheck(self):
        self.radio_check.check()

    def checkbox(self):
        self.check_box.check()


    def continue_buton(self):
        self.click_continue.click()

    def confirmation_msg(self):
        return self.msg_confirmation







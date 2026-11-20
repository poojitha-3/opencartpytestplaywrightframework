from playwright.sync_api import Page

class Homepage:
    def __init__(self, page:Page):
        self.page = page
        self.link_of_my_account=self.page.locator("a[title='My Account']")
        self.link_register=self.page.locator("a[href='https://tutorialsninja.com/demo/index.php?route=account/register']")
        self.link_login=self.page.locator("a[href='https://tutorialsninja.com/demo/index.php?route=account/login']")
        self.enter_search_input = self.page.locator("input[placeholder='Search']")
        self.click_search_button = self.page.locator("button[class='btn btn-default btn-lg']")

    def home_page(self):
        title=self.page.title()
        return title

    def click_my_account(self):

        try:
            self.link_of_my_account.click()
        except Exception as e:
            print(f"exception while clicking my account: {e}")
            raise

    def register_page(self):
        try:
            self.link_register.click()
        except Exception as e:
            print(f"exception while clicking register page: {e}")
            raise

    def login_page(self):
        try:
            self.link_login.click()
        except Exception as e:
            print(f"exception while clicking login page: {e}")
            raise

    def enter_input_in_search_box(self,search_input):
        self.enter_search_input.fill(search_input)

    def search_button(self):
        self.click_search_button.click()



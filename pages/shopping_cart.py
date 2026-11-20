from playwright.sync_api import Page

class ShoppingCart:
    def __init__(self,page:Page):
        self.page=page
        self.total_price=self.page.locator("//body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[2]")
        self.checkout=self.page.locator("a[class='btn btn-primary']")

    def total(self):
        try:
            return self.total_price.text_content()
        except Exception as e:
            print(f"error in total price: {e}")

    def checkout_button(self):
        try:
            self.checkout.click()
        except Exception as e:
            print(f"error in checkout button: {e}")
            
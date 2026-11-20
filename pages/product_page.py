from playwright.sync_api import Page
from pages.shopping_cart import ShoppingCart
class ProductPage:
    def __init__(self,page: Page):
        self.page = page
        self.txt_quantity=self.page.locator("#input-quantity")
        self.add_to_cart=self.page.locator("#button-cart")
        self.alert_msg=self.page.locator(".alert.alert-success.alert-dismissible")
        self.cart=self.page.locator("#cart")
        self.view_cart=self.page.locator("a:has-text('View Cart')")

    def product_quantity(self,qty):
        self.txt_quantity.fill("")
        self.txt_quantity.fill(qty)

    def add_cart(self):
        self.add_to_cart.click()

    def success_message(self):
        return self.alert_msg

    def items_cart(self):
        self.cart.click()

    def cart_view(self):
        self.view_cart.click()
        return ShoppingCart(self.page)

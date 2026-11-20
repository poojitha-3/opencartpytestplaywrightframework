from playwright.sync_api import Page
from pages.product_page import ProductPage

class SearchResultsPage:
    def __init__(self,page: Page):
        self.page = page

        self.txt_search=self.page.locator("h1:has-text('Search - ')")
        self.search_product=self.page.locator("h4 a")




    def get_page_header(self):
        try:
            return self.txt_search
        except Exception as e:
            print(f"exception while getting page header: {e}")

    def search_product_name(self,product_name):
        counts=self.search_product.count()

        for i in range(counts):
            product=self.search_product.nth(i)
            product_text=product.text_content().strip()
            if product_text==product_name:
                return product
        return None

    def select_product_name(self,product_name):
        counts=self.search_product.count()
        for i in range(counts):
            product=self.search_product.nth(i)
            product_text=product.text_content().strip()
            if product_text==product_name:
                product.click()
                return ProductPage(self.page)
        return None



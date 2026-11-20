import pytest

from pages.home_page import Homepage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from playwright.sync_api import expect
from config import Config
@pytest.mark.sanity
def test_add_to_cart(page):
    homepage = Homepage(page)
    homepage.enter_input_in_search_box(Config.product_name)
    homepage.search_button()

    search_results = SearchResultsPage(page)
    search_results.search_product_name(Config.product_name)
    search_results.select_product_name(Config.product_name)

    product_page = ProductPage(page)
    product_page.product_quantity(Config.product_quantity)
    product_page.add_cart()
    success_msg=product_page.success_message()
    expect(success_msg).to_be_visible(timeout=3000)
    product_page.items_cart()
    product_page.cart_view()

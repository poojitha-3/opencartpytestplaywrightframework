import pytest
from playwright.sync_api import expect
from pages.search_results_page import SearchResultsPage
from config import Config
from pages.home_page import Homepage
@pytest.mark.sanity
def test_search(page):
    search_page=SearchResultsPage(page)
    home_page=Homepage(page)

    product_name= Config.product_name
    home_page.enter_input_in_search_box(product_name)
    home_page.search_button()

    header=search_page.get_page_header()
    expect(header).to_be_visible(timeout=3000)

    search=search_page.search_product_name(product_name)
    expect(search).to_be_visible(timeout=3000)


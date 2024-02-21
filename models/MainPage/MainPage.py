import urllib.parse
from undetected_chromedriver import Chrome

from models.Product.Product import Product
from consts import URL

class MainPage:
    def __init__(self, browser: Chrome):
        self._browser = browser

    def search_product(self, product: Product):
        search_query = product.get_name()
        encoded_search_query = urllib.parse.quote(search_query)
        configured_url = self._get_configured_search_query(search_query=encoded_search_query)

        self._browser.get(configured_url)
        print(f"\nПоиск по {search_query}")

    def _get_configured_search_query(self, search_query: str):
        return f"{URL}/catalog/0/search.aspx?page=1&sort=rate&search={search_query}"
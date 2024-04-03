import urllib.parse

from basic_decor_library.Browser import Browser
from basic_decor_library.ExportProduct import ExportProduct
from models.MarketplaceParserProduct.MarketplaceParserProduct import MarketplaceParserProduct
from consts import URL

class MainPage(Browser):
    def __init__(self):
        super().__init__()

    def search_product(self, product: MarketplaceParserProduct):
        # search_query = product.get_name()
        search_query = product.name
        encoded_search_query = urllib.parse.quote(search_query)
        configured_url = self._get_configured_search_query(search_query=encoded_search_query)

        self._browser.get(configured_url)
        print(f"\nПоиск по {search_query}")

    def _get_configured_search_query(self, search_query: str):
        return f"{URL}/catalog/0/search.aspx?page=1&sort=rate&search={search_query}"

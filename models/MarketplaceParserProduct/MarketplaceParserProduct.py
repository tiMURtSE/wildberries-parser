from basic_decor_library.ExportProduct import ExportProduct
from typing import List
from basic_decor_library.ExportProductProperty import ExportProductProperty

class MarketplaceParserProduct(ExportProduct):
    def __init__(self, id: int, name: int, series: str, properties: List[ExportProductProperty]):
        super().__init__(id=id, name=name, series=series, properties=properties)
        self._page_links = []
        self._reviews = []
        
    @property
    def page_links(self):
        return self._page_links
    
    @page_links.setter
    def page_links(self, value):
        self._page_links = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value

    def get_name(self):
        return f"{self.series} {self.properties['Артикул']}"
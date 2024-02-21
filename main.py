import undetected_chromedriver as uc
import time

import my_library
from models.WorksheetConverter.WorksheetConverter import WorksheetConverter
from models.Page.Page import Page
from models.MainPage.MainPage import MainPage
from models.SearchResultPage.SearchResultPage import SearchResultPage
from models.ProductPage.ProductPage import ProductPage
from models.ReviewsPage.ReviewsPage import ReviewsPage
from consts import URL

class Main:
    def __init__(self):
        self._page = Page()
        self._main_page = MainPage()
        self._search_result_page = SearchResultPage()
        self._product_page = ProductPage()
        self._reviews_page = ReviewsPage()
        self._export_workbook = my_library.ExportWorkbook()
        self._worksheet_converter = WorksheetConverter()

    def run(self):
        self._page.get(URL)
        sheet = self._export_workbook.get_data()
        products = self._worksheet_converter.convert_to_products(sheet=sheet)

        for product in products:
            self._main_page.search_product(product=product)
            product_page_links = self._search_result_page.get_product_page_links()
            filtered_product_page_links = list(filter(lambda page_link: page_link, product_page_links))

            for page_link in filtered_product_page_links:
                self._page.get(page_link)
                self._product_page.go_to_reviews_page()
                reviews = self._reviews_page.get_reviews(product=product)
                product.reviews.extend(reviews)
                time.sleep(1)

            # time.sleep(3)
            print(f"Отзыв: {product.reviews}")
            
        self._page.quit()

if __name__ == "__main__":
    app = Main()
    app.run()
from basic_decor_library.Workbook import Workbook
from basic_decor_library.Browser import Browser
from models.MainPage.MainPage import MainPage
from models.SearchResultPage.SearchResultPage import SearchResultPage
from models.ProductPage.ProductPage import ProductPage
from models.ReviewsPage.ReviewsPage import ReviewsPage
from models.ResultWorkbook.ResultWorkbook import ResultWorkbook
from models.Error.Error import Error

from consts import URL

class Main:
    def __init__(self):
        self._export_workbook = Workbook()
        self._browser = Browser()
        self._main_page = MainPage()
        self._search_result_page = SearchResultPage()
        self._product_page = ProductPage()
        self._reviews_page = ReviewsPage()
        self._result_workbook = ResultWorkbook()
        self._error = Error()

    def run(self):
        self._browser.get(URL)
        product_property_names = ["Артикул"]
        products = self._export_workbook.create_products_from_excel_data(start_pos=3, product_property_names=product_property_names)
        start_pos = int(input("Номер товара, с которого нужно начать прохождение парсинг:\n"))

        for product in products[start_pos:]:
            print(product.__dict__)
            self._main_page.search_product(product=product)
            product.page_links = self._search_result_page.get_product_page_links()

            if not product.page_links:
                print("Нужных товаров не было найдено")
                continue

            for page_link in product.page_links:
                self._browser.get(page_link)
                self._product_page.go_to_reviews_page()
                reviews = self._reviews_page.get_reviews(product=product)
                product.reviews.extend(reviews)

            if product.reviews:
                print(f"Количество отзывов: {len(product.reviews)}")
                self._result_workbook.write_result(product=product)
            
        self._browser.quit()
        self._error.print_failed_product()

if __name__ == "__main__":
    app = Main()
    app.run()
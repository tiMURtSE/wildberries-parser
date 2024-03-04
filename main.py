from my_library import Workbook
from models.WorksheetConverter.WorksheetConverter import WorksheetConverter
from models.Page.Page import Page
from models.MainPage.MainPage import MainPage
from models.SearchResultPage.SearchResultPage import SearchResultPage
from models.ProductPage.ProductPage import ProductPage
from models.ReviewsPage.ReviewsPage import ReviewsPage
from models.ResultWorkbook.ResultWorkbook import ResultWorkbook
from models.Error.Error import Error
from consts import URL

class Main:
    def __init__(self):
        self._page = Page()
        self._main_page = MainPage()
        self._search_result_page = SearchResultPage()
        self._product_page = ProductPage()
        self._reviews_page = ReviewsPage()
        self._export_workbook = Workbook()
        self._result_workbook = ResultWorkbook()
        self._worksheet_converter = WorksheetConverter()
        self._error = Error()

    def run(self):
        self._page.get(URL)
        sheet = self._export_workbook.get_data()
        products = self._worksheet_converter.convert_to_products(sheet=sheet)
        start_pos = int(input("Номер строки, с которой нужно начать прохождение по товарам:\n"))

        for product in products[start_pos:]:
            self._main_page.search_product(product=product)
            product.page_links = self._search_result_page.get_product_page_links()

            if not product.page_links:
                print("Нужных товаров не было найдено")
                continue

            for page_link in product.page_links:
                self._page.get(page_link)
                self._product_page.go_to_reviews_page()
                reviews = self._reviews_page.get_reviews(product=product)
                product.reviews.extend(reviews)

            if product.reviews:
                print(f"Количество отзывов: {len(product.reviews)}")
            
        self._page.quit()
        self._error.print_failed_product()
        self._result_workbook.write_result(products=products)

if __name__ == "__main__":
    app = Main()
    app.run()
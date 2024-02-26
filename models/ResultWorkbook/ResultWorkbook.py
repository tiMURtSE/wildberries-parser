from typing import List
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

from models.Product.Product import Product
from models.Review.Review import Review

class ResultWorkbook:
    RESULT_WORKBOOK_FILE_PATH = "C:/Users/user10/Desktop/Stuff/Отзывы/Wildberries/Новые отзывы (Wildberries).xlsx"

    def __init__(self):
        self._workbook = openpyxl.load_workbook(self.RESULT_WORKBOOK_FILE_PATH)
        self._sheet: Worksheet = self._workbook.active
        self._start_position = self._define_start_position()

    def write_result(self, products: List[Product]):
        current_row_index = 0

        for product in products:
            for review in product.reviews:
                row_index = current_row_index + self._start_position
                self._write_review(row_index=row_index, review=review, product=product)
                current_row_index += 1

        self._workbook.save(self.RESULT_WORKBOOK_FILE_PATH)

    def _write_review(self, row_index: int, review: Review, product: Product):
        self._sheet.cell(row=row_index, column=2).value = product.id
        self._sheet.cell(row=row_index, column=15).value = product.article

        self._sheet.cell(row=row_index, column=4).value = review._customer_name
        self._sheet.cell(row=row_index, column=6).value = review._comment
        self._sheet.cell(row=row_index, column=11).value = review._rate

    def _define_start_position(self):
        return self._sheet.max_row + 1
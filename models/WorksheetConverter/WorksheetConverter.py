from openpyxl.worksheet.worksheet import Worksheet

from typing import List
from models.Product.Product import Product

class WorksheetConverter:
    PRODUCT_TABLE_START_POS = 3

    def convert_to_products(self, sheet: Worksheet):
        products: List[Product] = []

        for row in sheet.iter_rows(min_row=self.PRODUCT_TABLE_START_POS):
            product = Product(row=row)
            products.append(product)

        return products
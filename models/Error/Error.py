from models.Product.Product import Product

class Error:
    def __init__(self):
        self._failed_products = []

    def print_failed_product(self):
        if self._failed_products:
            print("Товары, при парсинге которых произошла ошибка:")
            print([product for product in self._failed_products])
        else:
            print("Все товары были спарсены")

    def set_failed_product(self, error: str, product: Product):
        failed_product = self._create_failed_product(error=error, product=product)
        self._failed_products.append(failed_product)

    def _create_failed_product(self, error: str, product: Product):
        return {
            "error_message": error,
            "product_id": product.id,
            "product_name": product.get_name()
        }
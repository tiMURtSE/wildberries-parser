from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Browser import Browser
from models.Product.Product import Product
from models.ReviewElement.ReviewElement import ReviewElement
from models.Error.Error import Error

class ReviewsPage(Browser):
    REVIEW_CLASS = "comments__item"
    SORTING_CLASS = "product-feedbacks__sorting"

    def __init__(self):
        super().__init__()
        self._review_element = ReviewElement()
        self._error = Error()

    def get_reviews(self, product: Product):
        reviews = []

        if not self._has_reviews():
            print(f"Нет отзывов для товара {product.get_name()}")
            return reviews
        
        self._scroll_to_bottom()

        review_elements = self._browser.find_elements(By.CLASS_NAME, self.REVIEW_CLASS)

        for review_element in review_elements:
            try:
                review = self._review_element.get_review(review_element=review_element, product=product)
            except Exception as e:
                self._error.set_failed_product(error=e, product=product)
                print(f"Ошибка у товара {product.get_name()}: {e}")
                continue

            reviews.append(review)

        return reviews

    def _has_reviews(self):
        try:
            self._wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, self.SORTING_CLASS))
            )
        except TimeoutException:
            return False
        
        return True
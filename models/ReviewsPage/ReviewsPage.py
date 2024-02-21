import time
from undetected_chromedriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from models.Product.Product import Product
from models.ReviewElement.ReviewElement import ReviewElement
from consts import ELEMENT_SEARCH_DELAY

class ReviewsPage:
    REVIEW_CLASS = "comments__item"
    SORTING_CLASS = "product-feedbacks__sorting"
    SCROLL_HEIGHT = "document.body.scrollHeight"
    COMMENT_CLASS = "comments__item"

    def __init__(self, browser: Chrome):
        self._browser = browser
        self._wait = WebDriverWait(browser, ELEMENT_SEARCH_DELAY)
        self._review_element = ReviewElement()

    def get_reviews(self, product: Product):
        reviews = []

        if not self._has_reviews():
            print(f"Нет отзывов для товара {product.get_name()}")
            return reviews
        
        self._scroll_to_bottom()

        review_elements = self._browser.find_elements(By.CLASS_NAME, self.REVIEW_CLASS)

        for review_element in review_elements:
            review = self._review_element.get_review(review_element=review_element, product=product)
            reviews.append(review)

        return reviews

    def _scroll_to_bottom(self):
        self._wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.COMMENT_CLASS)))

        while True:
            initial_scroll_height = self._browser.execute_script(f"return {self.SCROLL_HEIGHT}")
            self._browser.execute_script(f"window.scrollTo(0, {self.SCROLL_HEIGHT});")
            
            time.sleep(0.5)
            
            if self._browser.execute_script(f"return {self.SCROLL_HEIGHT}") == initial_scroll_height:
                break

    def _has_reviews(self):
        try:
            self._wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, self.SORTING_CLASS))
            )
        except TimeoutException:
            return False
        
        return True
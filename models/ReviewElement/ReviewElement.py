from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from models.Review.Review import Review
from models.Product.Product import Product

class ReviewElement:
    CUSTOMER_NAME_CLASS = "feedback__header"
    COMMENT_CLASS = "feedback__text"
    RATING_CLASS = "feedback__rating"

    def get_review(self, review_element: WebElement, product: Product):
        customer_name = self._get_customer_name(review_element=review_element)
        comment = self._get_comment(review_element=review_element)
        rate = self._get_rate(review_element=review_element)
        review_info = {
            "customer_name": customer_name,
            "comment": comment,
            "rate": rate,
        }

        review = Review(product_id=product.id, review=review_info)

        return review

    def _get_customer_name(self, review_element: WebElement):
        customer_name_element = review_element.find_element(By.CLASS_NAME, self.CUSTOMER_NAME_CLASS)
        customer_name = customer_name_element.text

        return customer_name

    def _get_comment(self, review_element: WebElement):
        comment_element = review_element.find_element(By.CLASS_NAME, self.COMMENT_CLASS)
        comment = comment_element.text

        return comment
    
    def _get_rate(self, review_element: WebElement):
        rate_element = review_element.find_element(By.CLASS_NAME, self.RATING_CLASS)
        rate_element_classname = rate_element.get_attribute("class")
        rate = self._extract_rate_from_classname(classname=rate_element_classname)

        return rate
    
    def _extract_rate_from_classname(self, classname: str):
        rate = int(classname.split()[-1][-1:])

        return rate
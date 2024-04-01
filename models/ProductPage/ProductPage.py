from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from basic_decor_library.Browser import Browser

class ProductPage(Browser):
    REVIEWS_PAGE_LINK_ID = "comments_reviews_link"

    def __init__(self):
        super().__init__()

    def go_to_reviews_page(self):
        reviews_page_link = self._wait.until(
            EC.presence_of_element_located((By.ID, self.REVIEWS_PAGE_LINK_ID))
        )

        reviews_page_link.click()
from undetected_chromedriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from consts import ELEMENT_SEARCH_DELAY

class ProductPage:
    REVIEWS_PAGE_LINK_ID = "comments_reviews_link"

    def __init__(self, browser: Chrome):
        self._browser = browser
        self._wait = WebDriverWait(browser, ELEMENT_SEARCH_DELAY)

    def go_to_reviews_page(self):
        reviews_page_link = self._wait.until(
            EC.presence_of_element_located((By.ID, self.REVIEWS_PAGE_LINK_ID))
        )

        reviews_page_link.click()
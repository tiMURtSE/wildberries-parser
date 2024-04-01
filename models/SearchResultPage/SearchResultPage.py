from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from basic_decor_library.Browser import Browser

class SearchResultPage(Browser):
    PRODUCT_CARD_CLASS = "product-card.product-card--hoverable.j-card-item"
    PRODUCT_RATE_CLASS = "address-rate-mini.address-rate-mini--sm"
    PRODUCT_PAGE_LINK_CLASS = "product-card__link"
    SEARCH_RESULT_TEXT_CLASS = "searching-results__text"
    NOT_FOUND_HEADING_CLASS = "catalog-page__not-found"

    def __init__(self):
        super().__init__()

    def get_product_page_links(self):
        product_page_links = []
        product_cards = self._get_product_cards()

        if self._are_products_not_found():
            return product_page_links

        for card in product_cards:
            product_rate = self._find_product_rate(product_card=card)

            if product_rate:
                product_page_link = self._find_product_page_link(product_card=card)
                product_page_links.append(product_page_link)

        filtered_page_links = self._filter_page_links(page_links=product_page_links)
        
        return filtered_page_links

    def _get_product_cards(self):
        product_cards = self._wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, self.PRODUCT_CARD_CLASS))
        )

        return product_cards

    def _find_product_rate(self, product_card: WebElement):
        rate_element = product_card.find_element(By.CLASS_NAME, self.PRODUCT_RATE_CLASS)
        rate = rate_element.text

        return rate

    def _find_product_page_link(self, product_card: WebElement):
        link_element = product_card.find_element(By.CLASS_NAME, self.PRODUCT_PAGE_LINK_CLASS)
        link = link_element.get_attribute("href")

        return link
    
    def _are_products_not_found(self):
        search_result_text_element = self._browser.find_element(By.CLASS_NAME, self.SEARCH_RESULT_TEXT_CLASS)
        search_result_text = search_result_text_element.text

        not_found_heading = self._browser.find_elements(By.CLASS_NAME, self.NOT_FOUND_HEADING_CLASS)
        not_found_heading_with_suggestion = "ничего не нашлось" in search_result_text

        return not_found_heading or not_found_heading_with_suggestion
    
    def _filter_page_links(self, page_links):
        filtered_page_links = list(filter(lambda page_link: page_link, page_links))

        return filtered_page_links
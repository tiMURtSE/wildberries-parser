import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from models.MarketplaceParserProduct.MarketplaceParserProduct import MarketplaceParserProduct
from basic_decor_library.Browser import Browser

class ProductPage(Browser):
    REVIEWS_PAGE_LINK_ID = "comments_reviews_link"
    DESCRIPTION_LINK_CLASS = "product-page__btn-detail"
    DESCRIPTION_CLASS = "option__text"
    PARAM_CELL_VALUE = "td.product-params__cell"
    CLOSE_BUTTON_CLASS = "j-close.popup__close.close"

    def __init__(self):
        super().__init__()

    def go_to_reviews_page(self, product: MarketplaceParserProduct):
        if self._is_product_suitable(product=product):
            self._close_description_overlay()
            reviews_page_link = self._browser.find_element(By.ID, self.REVIEWS_PAGE_LINK_ID)
            reviews_page_link.click()
        else:
            print("Открытая страница товара не подходит")

    def _is_product_suitable(self, product: MarketplaceParserProduct):
        self._go_to_description()
        time.sleep(0.5)

        if self._is_article_in_description(product=product) or self._is_article_in_param_value(product=product):
            return True
        else:
            return False    

    def _go_to_description(self):
        description_link = None

        try:
            description_link = self._wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, self.DESCRIPTION_LINK_CLASS))
            )

            description_link.click()
        except TimeoutException:
            print("TimeoutException при переходе на страницу с отзывами")

    def _is_article_in_description(self, product: MarketplaceParserProduct):
        try:
            description_element = self._browser.find_element(By.CLASS_NAME, self.DESCRIPTION_CLASS)
            description = description_element.text
        except:
            print("Нет описания товара")
            return False

        if str(product.properties["Артикул"]).lower() in description.lower():
            return True
        else:
            return False
        
    def _is_article_in_param_value(self, product: MarketplaceParserProduct):
        param_values = self._browser.find_elements(By.CSS_SELECTOR, self.PARAM_CELL_VALUE)
             
        for param_value in param_values:
            if str(product.properties["Артикул"]).lower() in param_value.text.lower():
                return True
            
        return False
    
    def _close_description_overlay(self):
        try:
            close_button = self._browser.find_element(By.CLASS_NAME, self.CLOSE_BUTTON_CLASS)

            close_button.click()
        except:
            print("Кнопки закрытия description overlay не было найдено")

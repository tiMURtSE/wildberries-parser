import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from consts import ELEMENT_SEARCH_DELAY

class Page:
    _browser_instance = None

    def __init__(self):
        self._set_browser()
        self._wait = WebDriverWait(self._browser, ELEMENT_SEARCH_DELAY)

    def get(self, url: str):
        self._browser.get(url)

    def quit(self):
        self._browser.quit()

    def _set_browser(self):
        if Page._browser_instance:
            self._browser = Page._browser_instance
        else:
            self._browser = uc.Chrome()
            Page._browser_instance = self._browser

    def _scroll_to_bottom(self):
        SCROLL_HEIGHT = "document.body.scrollHeight"
        COMMENT_CLASS = "comments__item" 

        self._wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, COMMENT_CLASS)))

        while True:
            initial_scroll_height = self._browser.execute_script(f"return {SCROLL_HEIGHT}")
            self._browser.execute_script(f"window.scrollTo(0, {SCROLL_HEIGHT});")
            
            time.sleep(0.5)
            
            if self._browser.execute_script(f"return {SCROLL_HEIGHT}") == initial_scroll_height:
                break
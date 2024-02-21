import undetected_chromedriver as uc

class Page:
    _browser_instance = None

    def __init__(self):
        if Page._browser_instance:
            self._browser = Page._browser_instance
        else:
            self._browser = uc.Chrome()
            Page._browser_instance = self._browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageQAuto:
    def __init__(self, driver, url):
        self.url = url
        self._driver = driver

    def open_page(self):
        self._driver.get(self.url)

    def _button(self, locator, timeout, message=None):
        butt = (WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(locator), message=message))
        return butt

    def _modal(self, locator, timeout, message=None):
        modal = (WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator), message=message))
        return modal

    def _raw(self, text, locator, message=None):
        raw = (WebDriverWait(self._driver, timeout=10).until(EC.element_to_be_clickable(locator), message=message))
        raw.clear()
        raw.send_keys(text)
        return raw


from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_27.locators_np import LocatorsNP


class SearchPageNP:
    def __init__(self, driver, url="https://tracking.novaposhta.ua/#/uk"):
        self.url = url
        self._driver = driver

    def open_page(self):
        self._driver.get(self.url)

    def set_package_numb(self, package_id):
        package_input_raw = (WebDriverWait(self._driver, 2)
                             .until(EC.presence_of_element_located(LocatorsNP.package_input_raw_loc),
                                    message='Cant find package input!'))
        package_input_raw.send_keys(package_id)
        return self

    def click_search_button(self):
        search_button = (WebDriverWait(self._driver, 2)
                         .until(EC.element_to_be_clickable(LocatorsNP.search_button_loc),
                                message='Cant find or click search button!'))
        search_button.click()
        return self

    def check_package(self):
        try:
            package_pre_status_succ = (WebDriverWait(self._driver, 2)
                                       .until(EC.presence_of_element_located(LocatorsNP.package_pre_succ_loc),
                                              message='Cant find or click pre-success button!'))
            package_pre_status_succ.click()
            package_status_succ = (WebDriverWait(self._driver, 2)
                                   .until(EC.presence_of_element_located(LocatorsNP.package_succ_loc),
                                          message='Cant find status success element!'))
            return package_status_succ.text
        except TimeoutException :
            try:
                package_status_not_f = (WebDriverWait(self._driver, 2)
                                        .until(EC.presence_of_element_located(LocatorsNP.package_not_f_loc),
                                               message='Cant find status not found element!'))
                return package_status_not_f.text
            except:
                return "Невідома помилка або змінились локатори!"



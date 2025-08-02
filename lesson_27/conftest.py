import pytest
from selenium.webdriver import Chrome
from lesson_27.search_page_np import SearchPageNP


@pytest.fixture(scope="module")
def driver():
    driver = Chrome()
    driver.get("https://tracking.novaposhta.ua/#/uk")
    yield driver
    driver.quit()


@pytest.fixture
def search_page_np(driver):
    return SearchPageNP(driver=driver)
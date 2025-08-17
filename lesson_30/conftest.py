import pytest
from selenium.webdriver import Chrome
from lesson_30.product_page_qauto import ProductPageQAuto


@pytest.fixture(scope="module")
def driver():
    driver = Chrome()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()


@pytest.fixture
def product_page_qauto(driver):
    return ProductPageQAuto(driver=driver)

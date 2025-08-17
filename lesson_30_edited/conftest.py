import pytest
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import Chrome
from lesson_30_edited.product_page_qauto import ProductPageQAuto


@pytest.fixture(scope="module")
def driver():
    opts = Options()
    if os.getenv("HEADLESS", "1") == "1":
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--window-size=1920,1080")

    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium")
    if os.path.exists(chrome_bin):
        opts.binary_location = chrome_bin

    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(30)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()
# def driver():
#     driver = Chrome()
#     driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
#     yield driver
#     driver.quit()


@pytest.fixture
def product_page_qauto(driver):
    return ProductPageQAuto(driver=driver)


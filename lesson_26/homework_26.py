from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dz.html")
    yield driver
    driver.quit()


@pytest.mark.parametrize("id_frame, id_input, secret", [
        ("frame1", "input1", "Frame1_Secret"),
        ("frame2", "input2", "Frame2_Secret")])
def test_frame_actions(driver, id_frame, id_input, secret):
    driver.switch_to.frame(driver.find_element(By.ID, id_frame))

    username_field = driver.find_element(By.ID, id_input)
    time.sleep(1)
    assert username_field.is_displayed(), f"Поле {id_input} не відображується!"
    username_field.send_keys(secret)
    time.sleep(2)

    frame_button = driver.find_element(By.CSS_SELECTOR, f"button[onclick=\"verifyInput('{id_input}')\"]")
    assert frame_button.is_enabled(), f"Кнопка для {id_input} не активна!"
    frame_button.click()
    time.sleep(2)

    alert = Alert(driver)
    alert_text = alert.text
    assert "Верифікація пройшла успішно!" in alert_text, f"Текст алерта некорректный: {alert_text}"
    alert.accept()
    time.sleep(2)
    driver.switch_to.default_content()


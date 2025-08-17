import pytest
import allure
from faker import Faker


@allure.epic('Qauto site')
class TestAllure:
    @pytest.mark.qauto
    @allure.feature('Registration on site Qato')
    @allure.story('Correct data Registration')
    def test_positive_registration(self, product_page_qauto):
        fake_email = Faker().email()
        product_page_qauto.open_page()
        product_page_qauto.click_sign_in_button().click_registration_button()
        product_page_qauto.fill_registration_form('George', 'Kocherha', fake_email, 'Gg1234567')
        product_page_qauto.click_register_button()

    @pytest.mark.qauto
    @allure.feature('Registration on site Qato')
    @allure.story('Incorrect data Registration')
    @pytest.mark.parametrize("first_name,last_name,email,password,expected_error", [
        ("", "Doe", "test13134@example.com", "Test1234$", "Name required"),
        ("John", "", "test@example.com", "Test1234$", "Last name required"),
        ("John", "Doe", "invalid_email", "Test1234$", "Email is incorrect"),
        ("John", "Doe", "test@example.com", "123", "Password"),
    ])
    def test_negative_registration(self, product_page_qauto, first_name, last_name, email, password, expected_error):
        product_page_qauto.open_page()
        product_page_qauto.click_sign_in_button().click_registration_button()
        product_page_qauto.fill_registration_form(first_name, last_name, email, password)
        errors = product_page_qauto.get_error_messages()
        assert any(expected_error in error for error in errors), f"Expected '{expected_error}' in {errors}"




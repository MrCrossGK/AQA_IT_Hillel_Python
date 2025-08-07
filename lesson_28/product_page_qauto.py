from lesson_28.base_page_qauto import BasePageQAuto
from lesson_28.locators_qauto import LocatorsQAuto


class ProductPageQAuto(BasePageQAuto):
    def __init__(self, driver, url="https://qauto2.forstudy.space/"):
        super().__init__(driver, url)

    def open_page(self):
        self._driver.get(self.url)

    def click_sign_in_button(self):
        sign_in_button = self._button(locator=LocatorsQAuto.sign_in_button_loc,
                                      timeout=10, message='Cant find or click "Sign In" button!')
        sign_in_button.click()
        return self

    def click_registration_button(self):
        self._modal(locator=LocatorsQAuto.login_modal_loc, timeout=10, message='Cant find modal!')
        registration_button = self._button(locator=LocatorsQAuto.registration_button_loc,
                                           timeout=10, message='Cant find or click "Registration" button!')
        registration_button.click()
        return self

    def fill_registration_form(self, name, last_name, email, password):
        self._modal(locator=LocatorsQAuto.login_modal_loc, timeout=10, message='Cant find modal!')
        self._raw(text=name, locator=LocatorsQAuto.name_raw_loc, message='Cant find "Name" raw!')
        self._raw(text=last_name, locator=LocatorsQAuto.last_name_raw_loc, message='Cant find "Last Name" raw!')
        self._raw(text=email, locator=LocatorsQAuto.email_loc, message='Cant find "Email" raw!')
        self._raw(text=password, locator=LocatorsQAuto.password_loc, message='Cant find "Password" raw!')
        self._raw(text=password, locator=LocatorsQAuto.re_password_loc, message='Cant find "Re-enter password" raw!')
        return self

    def click_register_button(self):
        self._modal(locator=LocatorsQAuto.login_modal_loc, timeout=10, message='Cant find modal!')
        register_button = self._button(locator=LocatorsQAuto.register_button_loc,
                                       timeout=10, message='Cant find or click "Register" button!')
        register_button.click()
        return self

    def get_error_messages(self):
        errors = self._driver.find_elements(*LocatorsQAuto.error_message_loc)
        return [error.text for error in errors if error.text.strip()]




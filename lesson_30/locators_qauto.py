from selenium.webdriver.common.by import By


class LocatorsQAuto:

    sign_in_button_loc = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')
    registration_button_loc = (By.XPATH, '//div[@class ="modal-footer d-flex justify-content-between"]'
                                         '/button[@class ="btn btn-link"]')
    login_modal_loc = (By.CSS_SELECTOR, ".modal-content")
    register_button_loc = (By.XPATH, '//button[@class="btn btn-primary"]')
    name_raw_loc = (By.NAME, 'name')
    last_name_raw_loc = (By.NAME, 'lastName')
    email_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    re_password_loc = (By.NAME, 'repeatPassword')
    error_message_loc = (By.CSS_SELECTOR, ".invalid-feedback")


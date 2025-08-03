from selenium.webdriver.common.by import By


class LocatorsNP:

    package_input_raw_loc = (By.XPATH, '//input[@class="track__form-group-input"]')
    search_button_loc = (By.XPATH, '//input[@class="track__form-group-btn green-active"]')
    package_pre_succ_loc = (By.CSS_SELECTOR, 'button[class="button v-btn v-btn--depressed'
                                             ' v-btn--flat v-btn--outlined theme--light v-size--default"]')
    package_succ_loc = (By.XPATH, '//div[@class="header__status-text"]')
    package_not_f_loc = (By.CSS_SELECTOR, 'div[err="[object Object]"] span')


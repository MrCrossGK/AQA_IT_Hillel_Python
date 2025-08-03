import pytest


@pytest.mark.parametrize("package_id, exp_resp", [
        ("20451213365377", "Отримана"),
        ("20451453365377", "Ми не знайшли посилку за таким номером."
                           " Якщо ви шукаєте інформацію про посилку,"
                           " якій більше 3 місяців, будь ласка,"
                           " зверніться у контакт-центр: 0 800 500 609")])
def test_package_search(driver, search_page_np, package_id, exp_resp):
    search_page_np.open_page()
    search_page_np.set_package_numb(package_id).click_search_button().check_package()
    result = search_page_np.check_package()
    print(f"\nСтатус посилки: {result}")
    assert exp_resp == result


import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

base_url = 'http://127.0.0.1:8080'

logger = logging.getLogger(__name__)
logging.getLogger("faker").propagate = False
logging.getLogger("urllib3").propagate = False


@pytest.fixture(scope='class')
def auth_func():
    logger.info("Виконується авторизація користувача")
    resp = requests.post(
        url=f'{base_url}/auth',
        auth=HTTPBasicAuth(username='test_user', password='test_pass')
    ).json()
    logger.debug(f"Отримано токен: {resp}")
    yield resp


@pytest.mark.usefixtures("auth_func")
class TestCarsApi:
    # Позитивні кейси
    @pytest.mark.parametrize("sort_by, limit", [("brand", 5),  # валідні значення
                                                ('brand', 10),  # валідні значення
                                                ('brand', 21),  # валідні значення
                                                ("brand", 0),  # граничні значення
                                                ("brand", 25),  # вся база
                                                (None, 3),  # без sort_by
                                                ("brand", None)])  # без limit
    def test_positive_cases(self, auth_func, sort_by, limit):
        logger.info(f"Позитивний тест із параметрами: sort_by={sort_by}, limit={limit}")
        headers = {'Authorization': f"Bearer {auth_func['access_token']}"}
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        resp = requests.get(f"{base_url}/cars", headers=headers, params=params)
        logger.debug(f"Отримано статус: {resp.status_code}, відповідь: {resp.text}")
        data = resp.json()

        assert isinstance(data, list), "Відповідь повинна бути списком!"
        logger.info(f"Отримані дані являються списком.")

        if limit is not None:
            assert len(data) <= int(limit), f"Limit перевищено: {len(data)} > {limit}"
            logger.info(f"Отримана довжина даних: {len(data)}, очікуваний ліміт: {limit}")

        if sort_by == "brand" and len(data) > 1:
            sorted_data = sorted(data, key=lambda x: x["brand"])
            assert data == sorted_data, "Данні не відсортовані по 'brand'"
            logger.info(f"Отримані дані із параметрами: sort_by={sort_by}, limit={limit}, відсортовані вірно.")

    # Негативні кейси
    @pytest.mark.parametrize("sort_by, limit, expected_res", [
        ("agssdd", 5, 200),
        ("", 5, 200),
        ("brand", -3, 200), # Тут до речі Flask app дозволяє приймати мінусові значення, тож виглядає як бажина)
        ("brand", "abc", 500),
        ("ololol", "xyz", 500)])
    def test_negative_cases(self, auth_func, sort_by, limit, expected_res):
        logger.info(f"Негативний тест: sort_by={sort_by}, limit={limit}, очікуваний статус код: {expected_res}")
        headers = {'Authorization': f"Bearer {auth_func['access_token']}"}
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        resp = requests.get(f"{base_url}/cars", headers=headers, params=params)
        if resp.status_code != expected_res:
            logger.error(
                f"Статус код не відповідає очікуваному! Очікувався: {expected_res}, отримано: {resp.status_code}")
        else:
            logger.debug(f"Статус код відповідає очікуваному: {expected_res}")

        assert resp.status_code == expected_res


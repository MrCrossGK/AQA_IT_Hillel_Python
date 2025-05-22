"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        # format='%(asctime)s - %(levelname)s - %(message)s',   # Це я додатково додав якби в лгу писався
                                                                # рівень логування, в кінці додав на це
                                                                # окрему перевірку
        force=True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


def read_file():  # Пишемо невеличку функцію для вичитки файла з логами
    with open("login_system.log", "r") as data:
        return data.read()


def clear_file():  # Цією функцією ми очищаємо (перезаписуємо) файл
    with open("login_system.log", "w") as data:
        data.write("")


@pytest.mark.parametrize("name,status",  # За допомогою параметрайз підставляємо певний набір тестових даних
                         [("Ann", "success"),
                          ("Sophia", "success"),
                          ("Sara", "expired"),
                          ("Andrew", "failed")])
def test_success(name, status):
    clear_file()  # Чистимо файл
    log_event(name, status)  # Викликаємо функцію з заданими тестовими аргументами що записує лог у файл
    exp_log_format = f"Login event - Username: {name}, Status: {status}"
    # Задаємо очікуваний формат логу з підставленими даними
    act_data = read_file()  # Вичитана строка з логом після відпрацювання функції log_event з заданими тестовими даними
    assert exp_log_format in act_data  # Перевіряємо чи очікуваний формат логу в вичитаній строці


# @pytest.mark.parametrize("name,status,exp_level",  # За допомогою параметрайз підставляємо певний набір тестових даних
#                          [("Ann", "success", "INFO"),
#                           ("Sara", "expired", "WARNING"),
#                           ("Andrew", "failed", "ERROR"),
#                           ("%99", "afa332", "ERROR")])
# def test_success(name, status, exp_level):
#     clear_file()  # Чистимо файл
#     log_event(name, status)  # Викликаємо функцію з заданими тестовими аргументами що записує лог у файл
#     exp_log_format = f"Login event - Username: {name}, Status: {status}"
#     # Задаємо очікуваний формат логу з підставленими даними
#     act_data = read_file()  # Вичитана строка з логом після відпрацювання функції log_event з заданими тестовими даними
#     assert exp_log_format in act_data  # Перевіряємо чи очікуваний формат логу в вичитаній строці
#     assert exp_level in act_data  # Додав додаткову перевірку очікуваного рівня логування на випадок не коректних даних

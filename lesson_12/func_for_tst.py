import logging

def is_palindrome(input_data):
    str_1 = list((input_data.lower()).replace(" ", ""))
    # str_1 = list(input_data.lower().replace(" ", ""))
    str_2 = list(reversed(input_data.lower().replace(" ", "")))

    # str_1 = ''.join(input_data.lower().split())  -> строка буез пробілів
    # return str_1 == str_1[::-1]
    print(str_1)
    if str_1 == str_2:
        return True
    else:
        return False


"""10) Дані про квитки (номер квитка, ціна, статус). 
Написати функцію, яка поверенре всі посилки у яких вказаний статус(задаеться при виклику функції) і задана ціна
tickets = [
    {"ticket_id": 1, "price": 100, "status": "sold"},
    {"ticket_id": 2, "price": 200, "status": "available"},
    {"ticket_id": 3, "price": 150, "status": "sold"},
    {"ticket_id": 4, "price": 250, "status": "available"}
]"""

tickets = [
    {"ticket_id": 1, "price": 100, "status": "sold"},
    {"ticket_id": 2, "price": 200, "status": "available"},
    {"ticket_id": 4, "price": 200, "status": None},
    {"ticket_id": 3, "price": 150, "status": "sold"},
    {"ticket_id": 4, "status": None},
    {"ticket_id": 5, "price": 250, "status": "available"},
    {"ticket_id": 6, "price": 0, "status": "available"},
    {"ticket_id": 7, "status": "available"}
]


def status_info(tic, price, status):
    logging.basicConfig(
        filename='logging_status.log',
        level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )
    logger = logging.getLogger("status_info")
    result = []
    for i in tic:
        try:
            if i["status"] == status and i["price"] == price:
                result.append(i)
            elif i["price"] == 0 or i["price"] is None:
                logger.warning(f'У квитка ticket_id - {i["ticket_id"]} не вказана ціна!')
            elif i["status"] is None:
                logger.warning(f"У квитка ticket_id - {i["ticket_id"]} не вказаний статус!")
        except KeyError:
            logger.error(f"Помилка, у ticket_id - {i["ticket_id"]}, не вказаний один або декілька із необхідних параметрів")

    return result


print(status_info(tickets, 250, "available"))

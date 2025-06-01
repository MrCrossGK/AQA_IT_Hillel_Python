from tools import address_assign
from pathlib import Path
import json


def is_valid_json():
    address_list = address_assign("json")  # Список адрес всіх json файлів
    for json_file_addr in address_list:  # Беремо кожну адресу і за допомогою try, підставляючи її намагаємось відкрити
        try:
            with Path(json_file_addr).open('r') as json_file:
                data = json.load(json_file)
                print(data)
        except UnicodeDecodeError as error:  # Не певний що правильно зробив але просто позапускав пару раз
                                             # та половив помилки і запхав в ексепти хз на скільки вірно XD
            print(f"При вичитці json файлу виникла помилка - {error}. !!!Алярама!!! ваш json файл - \"{json_file_addr.name}\" не валідний!")
        except json.decoder.JSONDecodeError as error:
            print(f"При вичитці json файлу виникла помилка - {error}. !!!Алярама!!! ваш json файл - \"{json_file_addr.name}\" не валідний!")


if __name__ == '__main__':
    is_valid_json()

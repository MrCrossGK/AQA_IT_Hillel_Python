from utils import address_assign, end_blank_remover  # Імпортуємо декілька функцій:
from pathlib import Path                             # 1) address_assign - повертає список всіх csv файлів
import csv                                           # у папці csv_lib.
                                                     # 2) end_blank_remover - прибирає зайвий "" у всіх
                                                     # строк у папці csv_lib.


def csv_dupl_rem():
    base_csv_file = []  # Створюємо пустий список куди закинемо всі строки з 2-х csv файлів
    res_csv_file = []  # Це список де будуть додані всі строки вже без дублікатів
    address_list = address_assign("csv")  # Список адрес всіх csv файлів

    for csv_file_addr in address_list:  # Проходимось по всім адресам списку csv файлів
        with Path(csv_file_addr).open(newline='') as csvfile:  # Почергово підставляємо назву файла для його вичитки
            data = end_blank_remover(list(csv.reader(csvfile)))  # Прибирає зайвий "" у всіх строк у папці csv_lib
            headers = data[0]
            rows = data[1:]
            for row in rows:  # Переганяємо кожну строку в тапл і додаємо в список, бо створити словник
                base_csv_file.append(tuple(row))  # з лістами не вийде

    base_csv_file = list(set(base_csv_file))  # Перетворюємо список з записами з 2-х csv файлів в множину і назад в ліст
                                              # щоб прибрати дублікати, отримуємо список з множинами
    for row in base_csv_file:  # Тут список з множинами знов перетворюємо на список з списками
        res_csv_file.append(list(row))

    res_csv_file.insert(0, headers)  # Додаємо хедер

    with open('result_kocherha.csv', 'w', newline='') as csvfile:  # Збираємо все назад і записуєм в окремий csv файл
        writer = csv.writer(csvfile)
        writer.writerows(res_csv_file)


if __name__ == '__main__':
    csv_dupl_rem()

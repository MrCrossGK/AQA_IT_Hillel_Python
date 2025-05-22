# task 1
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які
# присутні в lst1. Данні в лісті можуть бути будь якими


def is_sting_in_list(data: list) -> list[str]:
    lst2: list[str] = []
    for i in data:
        if isinstance(i, str):
            lst2.append(i)
    return lst2


if __name__ == '__main__':
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    print(f"\n{is_sting_in_list(lst1)}\n")

# Task 2
# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50”, ”qwerty1,2,3”, "1,2,3,4,50"]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити виняток
# і вивести “Не можу це зробити!”.
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”


def sum_func(data: list[int | str]) -> list[int | str]:
    res_list: list[int | str] = []
    for i in data:
        try:
            # Перебираємо кожен елемент entry_data, кожен елемент сплітаємо по
            # роздільнику "," та за допомогою вбудованої функції map() перетворюємо
            # в інт, (от тут, якщо крашиться, ловимо помилку й ідемо до наступного елемента)
            # перетворюємо в ліст і просумовуємо в кінці результат записуємо до попередньо
            # створенного списку res_list
            res_list.append(sum(list(map(int, i.split(",")))))
        except ValueError:
            res_list.append("Не можу це зробити")
        # Робимо except де очікуємо на певну помилку, в данному випадку ValueError і у разі її
        # виникнення, додаємо коментар до списку з результатом наших дій.
    return res_list


if __name__ == "__main__":
    entry_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "1,2,3,4,50"]
    print(sum_func(entry_data))


# Task 3
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.


def sum_even_numb(data: list[int]) -> int:
    even_numb: list[int] = []
    for i in data:
        if i & 1 == 0:  # Знайшов таке цікаве рішення, але ж працує!)
            even_numb.append(i)
    even_numb_sum = sum(even_numb)
    return even_numb_sum


if __name__ == "__main__":
    numb_list: list[int] = [32, 323, 3, 6, 8, 7, 1, 2, 5, 23, 37, 34, 7, 8, 392, 339]
    print(f"\nСума всіх парних чисел складає : {sum_even_numb(numb_list)}")


# Task 4
# Написати функцію, яка приймає список слів та повертає найдовше слово у списку.


def punct_mark_rem(data: str) -> list[str]:
    return data.replace(".", "").replace(",", "").split()
    # Створюємо функцію що повертає список слів де прибираємо крапки та коми


def longest_word(entry: list[str]) -> str:
    nums: list[int] = [len(i) for i in entry]  # Перетворюємо список слів, на список цифр, де цифра це довжина слова
    res: str = entry[(nums.index(max(nums)))]
    # Знаходимо найбільше число, знаходимо його індекс, та виводимо це слово підставивиши цей індекс у входження
    return res


if __name__ == '__main__':
    any_str = "Написати функцію, яка приймає рядок та повертає його у зворотньому порядку."
    mod_str = punct_mark_rem(any_str)
    print(f"\nНайдовше слово в списку: \"{longest_word(mod_str)}\"\n")


# Task 5
# Написати функцію, яка приймає рядок та повертає його у зворотному порядку.


def reverse_func(data: str) -> str:
    res: str = data[::-1]
    return res


if __name__ == '__main__':
    any_str = "Написати функцію, яка приймає рядок та повертає його у зворотньому порядку."
    print(reverse_func(any_str), f"\n")


# task 10
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements


def search_cars_by_criteria(car_data_dict: dict[str, tuple], search_crit_data: tuple) -> dict[str, tuple]:
    search_res: list = []  # Створюємо порожній список, куди будемо додавати елементи що відповідають search_criteria
    for i in car_data_dict.items():  # Перебираємо словник за ключем і значенням
        cd_year, cd_engine, cd_price = i[1][1], i[1][2], i[1][4]  # Рік, двигун, ціна в словнику car_data
        if cd_year >= search_crit_data[0] and cd_engine >= search_crit_data[1] and cd_price <= search_crit_data[2]:
            # Перевіряємо чи відповідає елемент заданим критеріям
            search_res.append(i)  # Якщо так, то додаємо до списку
    search_res: dict[str, tuple] = dict(search_res)  # Перетворюємо список назад в словник
    sorted_search_res = sorted(search_res.items(), key=lambda item: item[1][4])
    # Сортуємо словник за значенням
    sorted_search_res_5_elem: dict[str, tuple] = dict(sorted_search_res[:5])
    # Перші 5 елементів списку, на цьому можно було б закінчити, але я перфекціоніст, тому додав красивий прінт в кінці
    return sorted_search_res_5_elem


def organized_output(sorted_5_elem: dict[str, tuple]) -> None:
    print("Ось список із пеших 5ти автомобілів відсортованих за ціною, що задовольняють пошукові критерії:")
    for car_numb, car_details in enumerate(sorted_5_elem.items(), 1):
        colour, year, engine, car_type, price = car_details[1]
        model = car_details[0]
        print(f"{car_numb}. Автомобіль марки - {model}, колір - {colour},"
              f" рік випуску - {year}, об'єм двигуна - {engine},"
              f" тип кузова - {car_type}, вартість - {price} $.")


if __name__ == '__main__':
    car_data = {
        'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
        'Audi': ('black', 2020, 2.0, 'sedan', 55000),
        'BMW': ('white', 2018, 3.0, 'suv', 70000),
        'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
        'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
        'Honda': ('red', 2017, 1.5, 'sedan', 30000),
        'Ford': ('green', 2019, 2.3, 'suv', 40000),
        'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
        'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
        'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
        'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
        'Kia': ('white', 2020, 2.0, 'sedan', 28000),
        'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
        'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
        'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
        'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
        'Jeep': ('green', 2021, 3.0, 'suv', 50000),
        'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
        'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
        'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
        'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
        'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
        'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
        'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
        'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
        'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
        'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
        'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
        'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
        'Acura': ('white', 2017, 2.4, 'suv', 40000),
        'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
        'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
        'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
        'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
        'Ram': ('black', 2019, 5.7, 'pickup', 40000),
        'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
        'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
        'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
        'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
    }
    search_criteria = (2017, 1.6, 36000)
    print(search_cars_by_criteria(car_data, search_criteria), "\n")
    # organized_output(search_cars_by_criteria(car_data, search_criteria))

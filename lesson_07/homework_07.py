# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            print(f"The result - {result}, is greater than 25. Calculations are complete.\n")
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_func_0(a: int|float, b: int|float):
    res = a + b
    print(f"Сума двух чисел:\n {a} + {b} = {res}\n")


sum_func_0(4, 9)

# def sum_func(): # Просто альтернативне рішення з input
#     a = int(input("Введіть перший додаток - а\n"))
#     b = int(input("Введіть перший додаток - b\n"))
#     print(f"Сума двух чисел:\n {a} + {b} = {a + b}\n")
# sum_func()

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
rand_numb_lst = [23, 6, 123, 5, 93, 2, 5, 664, 13, 52, 48, 1, 9]
def arithmetic_mean(list):
    res = (sum(list)) / len(list)
    return res


print(f"Cереднє арифметичне списку чисел:\n{arithmetic_mean(rand_numb_lst):.3f}\n")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
any_str = "Написати функцію, яка приймає рядок та повертає його у зворотньому порядку."
def reverse_func(any_str: str):
    res = any_str[::-1]
    return res
print(reverse_func(any_str) + "\n")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
any_list = any_str.replace(".", "").replace(",", "").split() # Створюємо список слів де прибираємо крапки та коми
# print(any_list) # Додав цей прінт, щоб було видно список слів
def longest_word(entry):
    nums = [len(i) for i in entry] # Перетворюємо список слів, на список цифр, де цифра це довжина слова
    res = entry[(nums.index(max(nums)))] # Знаходимо найбільше число, знаходимо його індекс, та виводимо це слово підставивиши цей індекс у входження
    return res
print(longest_word(any_list) + "\n")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        index = str1.find(str2)
        return index
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10
# - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

def is_string_grater_10():
    some_string = input("Введіть будь яку строку:\n")
    if len(set(some_string)) > 10: # Множина не може мати дублікатів
    # print(len(set(some_string)), set(some_string))
        print(True)
    else:
        print(False)

is_string_grater_10()
# Написано будь-які то я і взяв цю, сподіваюсь це не буде помилкою, хоч тут
# явного входження в функцію немає, але є інпут, подумав що для різномаїття піде,
# якщо треба, можу переробити взявши інший приклад.

# task 8
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які
# присутні в lst1. Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
def is_sting_in_list(data):
    lst2 = []
    for i in lst1:
        if type(i) == str:
            lst2.append(i)
    print(f"\n{lst2}\n")

is_sting_in_list(lst1)

# task 9
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
numb_list = [32, 323, 3, 6, 8, 7, 1, 2, 5, 23, 37, 34, 7, 8, 392, 339]

def sum_even_numb(data):
    even_numb = []
    for i in numb_list:
        if i & 1 == 0: # Знайшов таке цікаве рішення, але ж працує!)
            even_numb.append(i)
    print(f"Сума всіх парних чисел складає : {sum(even_numb)}\n")

sum_even_numb(numb_list)

# task 10
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
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
def serch_cars_by_criteria(entry_data, search_criteria):
    search_res = [] # Створюємо пустий список, куди будемо додавати еслемнти що відповідають search_criteria
    for i in car_data.items(): # Перебираємо словник за ключем і значенням
        if i[1][1] >= search_criteria[0] and i[1][2] >= search_criteria[1] and i[1][4] <= search_criteria[2]: # Перевіряємо чи відповідає елемент заданим критеріям
            search_res.append(i) # Якщо так то додаєм до списку

    search_res = dict(search_res) # Перетворюємо список назад в словник
    sorted_search_res = sorted(search_res.items(), key=lambda item: item[1][4]) # Сортуємо словник за значенням (спочатку довго не міг зрозуміти як це зробити тому почав шукати в неті, знайшов рішення, а потім виявилось що в кінці теорії був саме такий приклад сортування XD lol)
    # print(dict(sorted_search_res)) # Весь відсортований список машин
    print(f"{dict(sorted_search_res[:5])}\n") # Перші 5 елементів списку, на цьому можно було б закінчити, але я перфекціоніст, тому додав красивий прінт в кінці

    sorted_search_res_5_elem = dict(sorted_search_res[:5]) #
    print("Ось список із пеших 5ти автомобілів відсортованих за ціною, що задовольняють пошукові критерії:")
    n = 1
    for i in sorted_search_res_5_elem.items():
        print(f"{n}. Автомобіль марки - {i[0]}, колір - {i[1][0]}, рік випуску - {i[1][1]}, об'єм двигуна - {i[1][2]}, тип кузова - {i[1][3]}, вартість - {i[1][4]} $.")
        n += 1

serch_cars_by_criteria(car_data, search_criteria)
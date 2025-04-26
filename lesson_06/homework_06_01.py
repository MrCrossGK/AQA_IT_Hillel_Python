# Порахувати кількість унікальних символів в строці. Якщо їх більше 10
# - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

some_string = input("Введіть будь яку строку:\n")
if len(set(some_string)) > 10: # Множина не може мати дублікатів
    # print(len(set(some_string)), set(some_string))
    print(True)
else:
    print(False)

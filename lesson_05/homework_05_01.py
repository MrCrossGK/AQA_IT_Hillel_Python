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

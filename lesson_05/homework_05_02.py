# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 1 - Add your new record o the beginning of the given list
people_records.insert(0, ("George", "Kocherha", 32, "Manual QA", "Kyiv")) # Додав свій новий запис за допомогою інсерт з індексом нуль щоб було першим в списку
# print(people_records)

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
swap_elem_1 = people_records.pop(5) # створюю змінну де розміщуємо елемент для свапу, почав з середини щоб не поїхали індекси
swap_elem_2 = people_records.pop(1) # так само з другим
people_records.insert(1, swap_elem_1) # тут просто вставив на потрібний індекс в звортоньому порядку
people_records.insert(5, swap_elem_2) # так само, можливо є більш елегантніше рішення, але воно працює
print(f"{people_records}\n")

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
# print(people_records[6][2], people_records[10][2], people_records[13][2])
age_check_list = [] # Пустий лист куди запишемо вік людей с заданимим індексами
age_check_list.append(people_records[6])
age_check_list.append(people_records[10])
age_check_list.append(people_records[13])

for i in age_check_list: # Ну і циклом прогнав список з перевіркою на вік
    name, surname, age, proffesion, city = i
    if i[2] >= 30:
        print(f"Yes, {name} {surname} is over 30 years old, she/he is {age} years old.")
    else:
        print(f"No, {name} {surname} is under 30 years old, she/he is {age} years old.")
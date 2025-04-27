lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
# Просто робимо цикл який перевіряє тип змінної, якщо стрінг, то додаєм в пустий ліст
for i in lst1:
    if type(i) == str:
        lst2.append(i)

print(lst2)
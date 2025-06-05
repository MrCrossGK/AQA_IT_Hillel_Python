class Student:

    def __init__(self, name: str, surname: str, age: int, aver_score: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.aver_score = aver_score
        self.answer = None

    def student_info(self):
        if self.answer is None:
            print(f"Стислі дані студента\nІм'я: {self.name}\nФамілія: {self.surname}\n"
                  f"Вік: {self.age}\nСередній бал (без пляхана): {self.aver_score}")
        elif self.answer == "так":
            print(f"Стислі дані студента\nІм'я: {self.name}\nФамілія: {self.surname}\n"
                  f"Вік: {self.age}\nСередній бал (з пляханом): {self.aver_score}")

    def set_aver_score(self):
        answer = input("Чи хочете ви змінити середній бал студента за пляхан?)\nНапишіть: Так чи Ні\n").lower()
        if answer == "так":
            new_value = input("Закинь прєподу пляшку на стіл і вкажи бажаний середній бал =)\n")
            self.aver_score = new_value
            self.answer = answer
        elif answer == "ні":
            print("Нє то нє, то такє, давай тоді шльопай звідси, та не роби мені нерви!)")
        else:
            print("Не має такого варіанту відповіді!")


if __name__ == "__main__":
    student_1 = Student("Василь", "Лагода", 18, 43)
    student_1.student_info()
    student_1.set_aver_score()
    student_1.student_info()

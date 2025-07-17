import random
from faker import Faker
from lesson_22.un_db import Course, Student, Relation


class University:

    def __init__(self, session):
        self.session = session
        self.courses_list = ['Math', 'History', 'Geometry', 'English', 'Spanish', 'Physics']
        self.course_ids = [id for (id,) in session.query(Course.id).all()]
        self.stud_ids = [id for (id,) in session.query(Student.id).all()]

    @property
    def rand_stud_id(self):
        return random.choice(self.stud_ids)

    @property
    def rand_course_id(self):
        return random.choice(self.course_ids)

    def stud_assign(self):
        relation = []

        for stud_id in self.stud_ids:
            selected_courses = random.sample(self.course_ids, k=random.randint(1, 3))
            for course_id in selected_courses:
                relation.append(Relation(student_id=stud_id, course_id=course_id))

        self.session.add_all(relation)
        self.session.commit()

    def stud_courses_disp(self):
        for student_id in self.stud_ids:
            relations = self.session.query(Relation).filter_by(student_id=student_id).all()
            for rel in relations:
                print(f"Студент {rel.student.student_name} записаний на курс {rel.course.course_name}")

    def course_stud_disp(self):
        for course_id in self.course_ids:
            relations = self.session.query(Relation).filter_by(course_id=course_id).all()
            for rel in relations:
                print(f"На курс {rel.course.course_name} записаний {rel.student.student_name}")

    def update_student(self):
        rand_stud_name = Faker().name()
        rand_id = self.rand_stud_id
        student = self.session.get(Student, rand_id)
        if student:
            student.student_name = rand_stud_name
            self.session.commit()
            print(f"Студент з id {rand_id} оновлений: {rand_stud_name}")
        else:
            print("Студент не знайден!")

    def update_course(self):
        addit_courses = ['Astronomy', 'Rocket_building', 'Python']
        rand_addit_course = random.sample(addit_courses, k=1)
        course = self.session.get(Course, self.rand_course_id)
        if rand_addit_course not in self.courses_list:
            course.course_name = rand_addit_course[0]
            self.session.commit()
            print(f"Курс с id {self.rand_course_id} обновлён: {rand_addit_course[0]}")
        else:
            print("Курс вже присутній!")

    def delete_student(self):
        student = self.session.get(Student, self.rand_stud_id)
        if student:
            self.session.query(Relation).filter_by(student_id=student.id).delete()
            self.session.delete(student)
            self.session.commit()
            print(f"Студент з id {self.rand_stud_id} видалений!")
        else:
            print("Студента не знайдено!")
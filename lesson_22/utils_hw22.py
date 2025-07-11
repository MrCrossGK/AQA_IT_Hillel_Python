from faker import Faker

from lesson_22.un_db import Course, Student


def add_courses(session):
    courses_list = ['Math', 'History', 'Geometry', 'English', 'Spanish', 'Physics']
    res = [Course(course_name=course) for course in courses_list]
    session.add_all(res)
    session.commit()


def add_students(session):
    res = [Student(student_name=Faker().name()) for i in range(20)]
    session.add_all(res)
    session.commit()
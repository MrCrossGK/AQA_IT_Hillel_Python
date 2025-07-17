from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random

DATABASE_URL = "postgresql://postgres:1313%40uro@localhost/dbhw22"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Relation(Base):
    __tablename__ = 'relations'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    courses = relationship("Relation", back_populates="student")


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    students = relationship("Relation", back_populates="course")


def add_courses():
    courses_list = ['Math', 'History', 'Geometry', 'English', 'Spanish', 'Physics']
    res = [Course(course_name=course) for course in courses_list]
    session.add_all(res)
    session.commit()


def add_students():
    res = [Student(student_name=Faker().name()) for i in range(20)]
    session.add_all(res)
    session.commit()


class University:

    def __init__(self):
        self.courses_list = ['Math', 'History', 'Geometry', 'English', 'Spanish', 'Physics']
        self.course_ids = [id for (id,) in session.query(Course.id).all()]
        self.stud_ids = [id for (id,) in session.query(Student.id).all()]
        self.rand_stud_id = random.sample(self.stud_ids, k=1)
        self.rand_course_id = random.sample(self.course_ids, k=1)

    def stud_assign(self):
        relation = []

        for stud_id in self.stud_ids:
            selected_courses = random.sample(self.course_ids, k=random.randint(1, 3))
            for course_id in selected_courses:
                relation.append(Relation(student_id=stud_id, course_id=course_id))

        session.add_all(relation)
        session.commit()

    def stud_courses_disp(self):
        for student_id in self.stud_ids:
            relations = session.query(Relation).filter_by(student_id=student_id).all()
            for rel in relations:
                print(f"Студент {rel.student.student_name} записаний на курс {rel.course.course_name}")

    def course_stud_disp(self):
        for course_id in self.course_ids:
            relations = session.query(Relation).filter_by(course_id=course_id).all()
            for rel in relations:
                print(f"На курс {rel.course.course_name} записаний {rel.student.student_name}")

    def update_student(self):
        rand_stud_name = Faker().name()
        student = session.get(Student, self.rand_stud_id)
        if student:
            student.student_name = rand_stud_name
            session.commit()
            print(f"Студент з id {self.rand_stud_id[0]} оновлений: {rand_stud_name}")
        else:
            print("Студент не знайден!")

    def update_course(self):
        addit_courses = ['Astronomy', 'Rocket_building', 'Python']
        rand_addit_course = random.sample(addit_courses, k=1)
        course = session.get(Course, self.rand_course_id[0])
        if rand_addit_course not in self.courses_list:
            course.course_name = rand_addit_course[0]
            session.commit()
            print(f"Курс с id {self.rand_course_id[0]} обновлён: {rand_addit_course[0]}")
        else:
            print("Курс вже присутній!")

    def delete_student(self):
        student = session.get(Student, self.rand_stud_id[0])
        if student:
            session.query(Relation).filter_by(student_id=student.id).delete()
            session.delete(student)
            session.commit()
            print(f"Студент з id {self.rand_stud_id[0]} видалений!")
        else:
            print("Студента не знайдено!")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    add_courses()
    add_students()
    uni = University()
    uni.stud_assign()
    uni.stud_courses_disp()
    uni.course_stud_disp()
    uni.update_student()
    uni.update_course()
    uni.delete_student()

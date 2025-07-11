from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


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
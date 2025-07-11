from sqlalchemy.orm import sessionmaker
from lesson_22.un_db import Base, engine
from lesson_22.university import University
from lesson_22.utils_hw22 import add_courses, add_students


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # add_courses(session)
    # add_students(session)
    uni = University(session)
    # uni.stud_assign()
    # uni.stud_courses_disp()
    # uni.course_stud_disp()
    # uni.update_student()
    # uni.update_course()
    # uni.delete_student()

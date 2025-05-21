from database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship


######## Zeyad: database ids should be UUIDs, not integers ########
# but sqllite does not support UUIDs natively, so integers will be fine for now
# or you can set the id as a str and add a UUID to it
# it's also better to use Mapped and mapped_column -> from sqlalchemy.orm import Mapped, mapped_column
# and then use id: Mapped[int] = mapped_column(primary_key=True)
# this will make it easier to use type checkers
# and also use the new style of defining relationships
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)
    enrollments = relationship("Enrollment", back_populates="student")


class Instructor(Base):
    __tablename__ = "instructors"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)
    courses = relationship("Course", back_populates="instructor")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    instructor = relationship("Instructor", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    progress = Column(Float, default=0.0)
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    # student can enroll in a course only once
    __table_args__ = (
        UniqueConstraint("student_id", "course_id", name="_student_course_uc"),
    )

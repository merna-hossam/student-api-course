from sqlalchemy import Column, Integer, String, ForeignKey, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

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
    __table_args__ = (UniqueConstraint('student_id', 'course_id', name='_student_course_uc'),)
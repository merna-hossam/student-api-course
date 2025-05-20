from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.course import CourseCreate, CourseUpdate, ProgressUpdate
from models import Course, Enrollment
from database import get_db

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("")
def create_course(data: CourseCreate, instructor_id: int, db: Session = Depends(get_db)):
    course = Course(title=data.title, description=data.description, instructor_id=instructor_id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@router.patch("/{course_id}")
def update_course(course_id: int, data: CourseUpdate, db: Session = Depends(get_db)):
    course = db.query(Course).filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if data.title:
        course.title = data.title
    if data.description:
        course.description = data.description
    db.commit()
    return {"message": "Course updated"}

@router.patch("/{course_id}/progress")
def update_progress(course_id: int, update: ProgressUpdate, db: Session = Depends(get_db)):
    course = db.query(Course).filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    enrollment = db.query(Enrollment).filter_by(course_id=course_id, student_id=update.student_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    enrollment.progress = update.percentage
    db.commit()
    return {"message": "Progress updated"}
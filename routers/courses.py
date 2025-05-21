from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import Course, Enrollment
from schemas.course import CourseCreate, CourseUpdate, ProgressUpdate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/courses", tags=["Courses"])


######## Zeyad: why not just have instructor_id in the courseCreate schema?#######
# also these endpoints should be protected
# I see you are using JWT, but you are not using it here to verify the user
@router.post("")
def create_course(
    data: CourseCreate, instructor_id: int, db: Session = Depends(get_db)
):
    course = Course(
        title=data.title, description=data.description, instructor_id=instructor_id
    )
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@router.patch("/{course_id}")
def update_course(course_id: int, data: CourseUpdate, db: Session = Depends(get_db)):
    course = db.query(Course).filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    # Zeyad: this will cause an error with type checkers because you didn't use Mapped in your database models
    if data.title:
        course.title = data.title
    if data.description:
        course.description = data.description
    db.commit()
    return {"message": "Course updated"}


@router.patch("/{course_id}/progress")
def update_progress(
    course_id: int, update: ProgressUpdate, db: Session = Depends(get_db)
):
    course = db.query(Course).filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    enrollment = (
        db.query(Enrollment)
        .filter_by(course_id=course_id, student_id=update.student_id)
        .first()
    )
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    enrollment.progress = update.percentage
    db.commit()
    return {"message": "Progress updated"}

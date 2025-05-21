from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import Enrollment, Student
from schemas.student import StudentCreate, StudentLogin
from sqlalchemy.orm import Session
from utils.auth import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/register")
def register_student(data: StudentCreate, db: Session = Depends(get_db)):
    if db.query(Student).filter(Student.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    student = Student(
        name=data.name, email=data.email, password=hash_password(data.password)
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"message": "Student registered", "id": student.id}


@router.post("/login")
def login_student(data: StudentLogin, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.email == data.email).first()
    if not student or not verify_password(data.password, student.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(student.id)})
    return {"access_token": token, "token_type": "bearer"}


############### Zeyad: these endpoints should be protected
# I see you are using JWT, but you are not using it here to verify the user
@router.get("/me/courses")
def my_courses(student_id: int, db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).filter(Enrollment.student_id == student_id).all()
    return [{"course_id": e.course_id, "progress": e.progress} for e in enrollments]


@router.post("/enroll")
def enroll(course_id: int, student_id: int, db: Session = Depends(get_db)):
    from models import Course

    if (
        db.query(Enrollment)
        .filter_by(student_id=student_id, course_id=course_id)
        .first()
    ):
        raise HTTPException(status_code=400, detail="Already enrolled")
    if not db.query(Course).filter_by(id=course_id).first():
        raise HTTPException(status_code=404, detail="Course not found")
    enroll = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enroll)
    db.commit()
    return {"message": "Enrolled successfully"}

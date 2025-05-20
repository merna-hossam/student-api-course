from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.instructor import InstructorCreate, InstructorLogin
from models import Instructor
from utils.auth import hash_password, verify_password, create_access_token
from database import get_db

router = APIRouter(prefix="/instructors", tags=["Instructors"])

@router.post("/register")
def register_instructor(data: InstructorCreate, db: Session = Depends(get_db)):
    if db.query(Instructor).filter(Instructor.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    instructor = Instructor(name=data.name, email=data.email, password=hash_password(data.password))
    db.add(instructor)
    db.commit()
    db.refresh(instructor)
    return {"message": "Instructor registered", "id": instructor.id}

@router.post("/login")
def login_instructor(data: InstructorLogin, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.email == data.email).first()
    if not instructor or not verify_password(data.password, instructor.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(instructor.id)})
    return {"access_token": token, "token_type": "bearer"}
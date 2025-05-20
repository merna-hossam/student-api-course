from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class StudentLogin(BaseModel):
    email: EmailStr
    password: str
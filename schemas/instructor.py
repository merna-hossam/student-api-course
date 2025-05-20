from pydantic import BaseModel, EmailStr

class InstructorCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class InstructorLogin(BaseModel):
    email: EmailStr
    password: str
from typing import Optional

from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    instructor_id: int


################### Zeyad: NEED TO ADD OPTIONAL IF YOU WANT IT TO BE NONE AS DEFAULT ####################
class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class ProgressUpdate(BaseModel):
    student_id: int
    percentage: float

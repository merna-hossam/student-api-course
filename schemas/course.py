from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str
    description: str

class CourseUpdate(BaseModel):
    title: str = None
    description: str = None

class ProgressUpdate(BaseModel):
    student_id: int
    percentage: float
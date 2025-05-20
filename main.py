from fastapi import FastAPI
from database import Base, engine
from routers import students, instructors, courses

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Course Enrollment & Progress Tracker API")

app.include_router(students.router)
app.include_router(instructors.router)
app.include_router(courses.router)
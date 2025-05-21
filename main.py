# routers for students, instructors, and courses
from database import Base, engine
from fastapi import FastAPI
from routers import courses, instructors, students

# Automatically create all database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Course Enrollment & Progress Tracker API")
############ Zeyad: You should usually use UV and add a pyproject.toml file to your project
# to manage dependencies easier
app.include_router(students.router)
app.include_router(instructors.router)
app.include_router(courses.router)

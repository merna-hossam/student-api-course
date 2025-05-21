Student Course Enrollment & Progress Tracker API

A fully functional backend API built with **FastAPI** that supports student and instructor workflows for a university course system.
Students can register, enroll in courses, and track progress. Instructors can manage courses and update student progress.

### Features

### Student Endpoints
- `POST /students/register`: Register a new student
- `POST /students/login`: Log in as a student (returns JWT)
- `GET /students/me/courses`: View enrolled courses with progress
- `POST /students/enroll`: Enroll in a course

### Instructor Endpoints
- `POST /instructors/register`: Register a new instructor
- `POST /instructors/login`: Log in as an instructor (returns JWT)
- `POST /courses`: Create a new course
- `PATCH /courses/{course_id}`: Edit an existing course
- `PATCH /courses/{course_id}/progress`: Update a student's progress

## Data Model

- `Student`: name, email, hashed password
- `Instructor`: name, email, hashed password
- `Course`: title, description, instructor_id
- `Enrollment`: course_id, student_id, progress (%)

## Tech Stack

- **Python 3.11+**
- **FastAPI** – modern web framework
- **SQLAlchemy** – ORM for database access
- **SQLite** – simple, local development DB
- **Pydantic** – for input validation
- **Passlib + bcrypt** – for password hashing
- **JWT (python-jose)** – for authentication

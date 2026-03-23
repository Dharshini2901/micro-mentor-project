# Micro Mentor - Peer-to-Peer Mentorship Platform

A full-stack web application built with Django that connects students (Mentees) with industry professionals (Mentors).

## Live Demo
- Website: https://micro-mentor-project.onrender.com
- API: https://micro-mentor-project.onrender.com/api/mentors/
- Admin: https://micro-mentor-project.onrender.com/admin/

## Screenshots

### Home Page
![Home](static/images/screenshot/home.png)

### Login Page
![Login](static/images/screenshot/login.png)

### Registration Page
![Registration](static/images/screenshot/registration.png)

### REST API
![API](static/images/screenshot/api.png)

### Admin Panel
![Admin](static/images/screenshot/admin.png)

## Tech Stack
- Language: Python 3.11
- Framework: Django 5.x
- REST API: Django REST Framework
- Authentication: Token Authentication
- Database: SQLite (Dev) / PostgreSQL (Production)
- Deployment: Render
- Static Files: WhiteNoise

## Features
- Dual-role authentication (Mentor and Mentee)
- Role-specific dashboards
- Mentorship request system
- Dynamic profile management
- REST API with 5 endpoints
- Token Authentication for API security
- Django Admin panel
- 17 automated tests

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | /api/login/ | No | Get auth token |
| GET | /api/mentors/ | No | List all mentors |
| GET | /api/mentors/id/ | No | Get mentor detail |
| GET | /api/bookings/ | Yes | List all bookings |
| GET | /api/users/ | Yes | List all users |

## API Usage

### Step 1 - Get Token
POST /api/login/
{
    "username": "your_username",
    "password": "your_password"
}
Response: {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}

### Step 2 - Use Token
GET /api/bookings/
Header: Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

## Run Locally
git clone https://github.com/Dharshini2901/micro-mentor-project.git
cd micro-mentor-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Run Tests
python manage.py test
Runs 17 tests covering accounts, mentors, and API endpoints.

## Project Structure
micro_mentor/
+-- accounts/      # Custom user model, auth
+-- mentors/       # Mentor profiles, bookings
+-- chat/          # Messaging feature
+-- api/           # REST API + Token Auth
+-- templates/     # HTML templates
+-- static/        # CSS, images, screenshots
+-- manage.py

## Developer
Dharshini DR - Python/Django Developer
GitHub: https://github.com/Dharshini2901
Email: dharshinidr05@gmail.com
LinkedIn: https://linkedin.com/in/dharshini-d-r-33158b255


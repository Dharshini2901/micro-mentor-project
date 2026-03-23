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
- Database: SQLite (Dev) / PostgreSQL (Production)
- Deployment: Render
- Static Files: WhiteNoise

## Features
- Dual-role authentication (Mentor and Mentee)
- Role-specific dashboards
- Mentorship request system
- Dynamic profile management
- REST API with 4 endpoints
- Django Admin panel
- 17 automated tests

## API Endpoints
- GET /api/mentors/ - List all mentors
- GET /api/mentors/id/ - Get mentor detail
- GET /api/bookings/ - List all bookings
- GET /api/users/ - List all users

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

## Developer
Dharshini DR - Python/Django Developer
GitHub: https://github.com/Dharshini2901
Email: dharshinidr05@gmail.com
LinkedIn: https://linkedin.com/in/dharshini-d-r-33158b255

# Django Project - Very Advanced Techniques in Django Templates (SSR)

##  Exam Project - Web Programming in Python (2025)
> Student: Ben Rhouma Nermine
> University: Sesame University  
> Professor: Chaouki Bayoudhi

---

## Description

This project implements advanced dynamic template rendering using Django with:
- Dynamic HTML components stored in database
- JSON-driven template rendering (SSR)
- REST and GraphQL APIs for CRUD
- Celery background task to pre-render components
- JWT-based authentication for API access
## Technologies Used
- Python 3.10+
- Django 4+
- Django REST Framework
- Graphene-Django (GraphQL)
- Celery + Redis
- djangorestframework-simplejwt (JWT)
## Installation (Local Setup)

### 1. Clone the project and create a virtual environment

python -m venv env
env\Scripts\activate  

### 2. Install dependencies
pip install -r requirements.txt
### 3. Apply database migrations
python manage.py migrate
### 4. Create superuser (for JWT login)
python manage.py createsuperuser

// JWT Authentication

### 5. Get a token (POST)
URL : http://127.0.0.1:8000/api/token/
Body :
json

{
  "username": "nermine",
  "password": "Z22ZrCa3i"
}
Add header for authenticated requests:
Authorization: Bearer ACCESS_TOKEN

// Celery + Redis (SSR Pre-rendering)
### 6. Start Redis (via Docker)

docker run -d -p 6379:6379 redis
### 7. Start Celery (Windows)

celery -A advanced_templates worker --loglevel=info --pool=solo

// Run Django server

python manage.py runserver
### 8. Tester l'API GraphQL
http://127.0.0.1:8000/graphql/





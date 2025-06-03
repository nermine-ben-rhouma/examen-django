# 🧠 Django Project – Very Advanced Techniques in Django Templates (SSR)

## 🎓 Exam Project – Web Programming in Python (2025)
> 👩‍🎓 Student: Ben Rhouma Nermine  
> 🏛️ University: Sesame University  
> 👨‍🏫 Professor: Chaouki Bayoudhi

---

## 📌 Description

This project implements advanced dynamic template rendering using Django:

- 🧱 Dynamic HTML components stored in the database
- 🔄 JSON-driven server-side rendering (SSR) using Django templates
- 🔐 JWT-protected REST API with DRF
- 🧪 GraphQL API via Graphene
- ⚙️ Celery background task for pre-rendering HTML
- 🤖 Local AI Integration using **TextBlob**

---

## 🛠️ Technologies Used

- Python 3.10+
- Django 4+
- Django REST Framework
- Graphene-Django (GraphQL)
- Celery + Redis
- djangorestframework-simplejwt (JWT)
- TextBlob (local AI sentiment analysis)

---

## ⚙️ Installation (Local Setup)

### 1. Clone the project and create a virtual environment

```bash
python -m venv env
env\Scripts\activate
2. Install dependencies
bash

pip install -r requirements.txt
3. Apply database migrations
bash

python manage.py migrate
4. Create a superuser
bash

python manage.py createsuperuser
🔐 JWT Authentication (Postman)
5. Get an access token
POST http://127.0.0.1:8000/api/token/
Body (raw / JSON):

json

{
  "username": "nermine",
  "password": "Z22ZrCa3i"
}
➡️ Add this to headers for authenticated requests:

makefile

Authorization: Bearer <ACCESS_TOKEN>
⚙️ Celery + Redis (for background tasks)
6. Start Redis (via Docker)
bash

docker run -d -p 6379:6379 redis
7. Start Celery (Windows)
bash
celery -A advanced_templates worker --loglevel=info --pool=solo
🚀 Start the Django server
bash

python manage.py runserver
🔎 GraphQL API (Optional)
8. Test GraphQL in browser
Open:

http://127.0.0.1:8000/graphql/
Example query:

graphql

{
  allComponents {
    id
    name
    renderedHtml
  }
}
🌍 Useful URLs
🔗 API REST: http://127.0.0.1:8000/api/components/

🖥️ SSR Render: http://127.0.0.1:8000/api/render/ID/

🔐 Admin panel: http://127.0.0.1:8000/admin/


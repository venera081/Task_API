#  Task Manager API

A production-style backend Task Management system built with Django REST Framework.
This project demonstrates real-world backend architecture including authentication, role-based access control, notifications, and scalable service design.

---

##  About Project

This API allows users to manage tasks, categories, companies, and team workflows with role-based permissions and automated notifications.

It is designed as a backend system similar to real SaaS products.

---

##  Key Features

*  JWT Authentication (Access & Refresh tokens)
*  Email confirmation system
*  Google OAuth login
*  Role-based access control:

  * Owner
  * Manager
  * Employee
*  Company management system
*  Task CRUD operations
*  Task categories
*  Subtasks support
*  Comments system
*  Automatic notifications on task updates
*  User statistics dashboard
*  Task status change logs
*  Filtering, search, and ordering
*  Rate limiting (throttling)
*  API documentation (Swagger & ReDoc)

---

##  Tech Stack

* Python 3.12
* Django 6
* Django REST Framework
* PostgreSQL / SQLite
* SimpleJWT
* drf-yasg (Swagger)
* Gunicorn
* Docker

---

##  Run with Docker

### 1. Build and run containers

```bash
docker compose up --build
```

---

### 2. Run migrations

```bash
docker compose exec web python manage.py migrate
```

---

### 3. Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

##  Installation (Local Setup)

### 1. Clone repository

```bash
git clone https://github.com/your-username/Task_Manager_API.git
cd Task_Manager_API
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password

GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_secret
GOOGLE_CLIENT_URI=your_redirect_uri
```

---

### 5. Apply migrations

```bash
python manage.py migrate
```

---

### 6. Run server

```bash
python manage.py runserver
```

---

##  API Documentation

* Swagger UI:
  http://127.0.0.1:8000/swagger/

* ReDoc:
  http://127.0.0.1:8000/redoc/

---

##  Authentication

JWT-based authentication system:

* Access Token: 15 minutes
* Refresh Token: 1 day

### Example header:

```http
Authorization: Bearer <your_token>
```

---

##  Main API Endpoints

###  Users

* `/api/v1/users/register/`
* `/api/v1/users/login/`
* `/api/v1/users/confirm-email/`

###  Tasks

* `/api/v1/tasks/`
* `/api/v1/tasks/{id}/`

###  Company

* `/api/v1/company/`

###  Notifications

* `/api/v1/notifications/`

###  Statistics

* `/api/v1/statistics_app/`

---

##  Architecture

The project follows clean backend architecture principles:

* Service Layer (business logic separation)
* Custom permissions system
* Modular Django apps:

  * users
  * tasks
  * company
  * notifications
  * statistics

---

##  Permissions System

* **Owner** → full access to system
* **Manager** → limited management access
* **Employee** → access only to own data

---

##  Highlights

* Task lifecycle tracking with logs
* Automatic notifications on status changes
* User statistics system
* Advanced filtering, search, ordering
* Request throttling for API protection

---

##  Deployment

Planned deployment:

* Render
* Railway
* VPS (Linux server)

---

##  Author

Backend Developer (Junior)

* Stack: Python, Django, DRF
* Goal: Work internationally as a backend engineer

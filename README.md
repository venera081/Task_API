# Task Manager API

A full-featured backend application for task management built with Django REST Framework.
Supports user roles, companies, tasks, notifications, and statistics.

---

##  Features

*  JWT Authentication (Access & Refresh tokens)
*  Email confirmation system
*  Google OAuth login
*  User roles:

  * Owner
  * Manager
  * Employee
*  Company management
*  Task CRUD operations
*  Task categories
*  Subtasks support
*  Comments system
*  Notifications
*  User statistics
*  Task status change logs
*  Filtering, search, and ordering
*  API documentation (Swagger & ReDoc)

---

##  Tech Stack

* Python 3.x
* Django 6
* Django REST Framework
* PostgreSQL / SQLite
* JWT (SimpleJWT)
* drf-yasg (Swagger)
* Gunicorn
* Docker (in progress)

---

##  Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Task_Manager_Api.git
cd Task_Manager_Api
```

---

### 2. Create virtual environment

```bash
python -m venv venv(or - python3 -m venv venv)
source venv/bin/activate(for Linux)
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create .env file

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

### 6. Run the server

```bash
python manage.py runserver
```

---

##  API Documentation

* Swagger:
  `http://127.0.0.1:8000/swagger/`

* ReDoc:
  `http://127.0.0.1:8000/redoc/`

---

##  Authentication

This project uses JWT authentication:

* Access Token (15 minutes)
* Refresh Token (1 day)

Header example:

```http
Authorization: Bearer <your_token>
```

---

##  Main Endpoints

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

The project follows clean architecture principles:

* Service Layer (business logic separated)
* Custom permissions
* Modular apps:

  * users
  * tasks
  * company
  * notifications
  * statistics

---

##  Permissions

* Owner — full access
* Manager — limited access
* Employee — only own data

---

##  Highlights

* Task status change logging
* Automatic notifications on status updates
* User task statistics
* Request throttling
* Advanced filtering and search

---

##  Docker

Docker support will be added soon.

---

##  Deployment

Planned deployment options:

* Render
* Railway
* VPS

---

##  Author

Backend Developer (Junior)
Stack: Python, Django, DRF
Goal: Work internationally as a backend engineer




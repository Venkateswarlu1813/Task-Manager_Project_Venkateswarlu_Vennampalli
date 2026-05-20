# Task Management System Backend

## Project Overview

This is a collaborative Task Management System backend developed using Django REST Framework.

The system supports:

- JWT Authentication
- Google Login
- Team Management
- Task Management
- Task Assignment
- Task Comments
- File Attachments
- Team Invitations
- Activity Logging
- Role-Based Access Control

---

# Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- Postman
- Swagger UI

---

# Features

## Authentication
- Register
- Login
- JWT Token Authentication
- Google OAuth Login

## Team Management
- Create Team
- Add Members
- Invite Members

## Task Management
- Create Task
- Update Task Status
- Assign Users
- Set Priority
- Set Due Date

## Collaboration
- Task Comments
- File Attachments
- Activity Logs

---

# API Endpoints

## Authentication

POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/google-login/

---

## Teams

GET /api/teams/
POST /api/teams/
POST /api/teams/add-member/
POST /api/teams/invite/

---

## Tasks

GET /api/tasks/
POST /api/tasks/
PATCH /api/tasks/<id>/update-status/

---

## Comments

GET /api/tasks/<id>/comments/
POST /api/tasks/<id>/comments/

---

## Attachments

POST /api/tasks/<id>/attachments/

---

# Swagger Documentation

Access Swagger UI:

http://127.0.0.1:8000/swagger/

---

# Database Modules

- Users
- Teams
- Team Members
- Team Invitations
- Tasks
- Task Assignees
- Task Comments
- Task Attachments
- Activity Logs

---

# Project Architecture

User → Team → Task → Comments / Attachments / Activity Logs

---

# How to Run

## Install dependencies

pip install -r requirements.txt

## Apply migrations

python manage.py makemigrations
python manage.py migrate

## Run server

python manage.py runserver

---

# Author

Venkateswarlu Vennampalli

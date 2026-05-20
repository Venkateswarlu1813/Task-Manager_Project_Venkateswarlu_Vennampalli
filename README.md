# Task Manager System

## Project Overview

The Task Manager System is a full-stack web application developed to help users manage daily tasks efficiently. The system allows users to create, update, delete, and monitor tasks in a simple and organized way.

The application also includes:

* Secure user authentication
* Google Login integration
* Task status management
* Separate custom admin dashboard
* SMTP email notifications
* Search and filter functionality
* Role-based access

This project was developed using Next.js for the frontend and Django REST Framework for the backend.

---

# Problem Statement

Managing tasks manually becomes difficult when multiple users are involved. Users may forget deadlines, lose track of pending tasks, or face difficulty organizing work.

This Task Manager System solves these problems by:

* Providing centralized task management
* Allowing users to track task progress
* Sending email notifications
* Giving administrators a monitoring dashboard
* Improving productivity and organization

---

# Objectives

The main objectives of this project are:

* To create a secure task management platform
* To provide user-friendly task tracking
* To implement role-based authentication
* To provide task analytics through an admin dashboard
* To send task notifications using SMTP
* To build a scalable frontend-backend architecture

---

# Technologies Used

## Frontend

* Next.js
* React.js
* Tailwind CSS
* React Hot Toast
* React Icons
* Google OAuth

## Backend

* Django
* Django REST Framework
* JWT Authentication
* SMTP Email Service
* Cloudinary (File Uploads)

## Database

* SQLite

---

# System Architecture

```text
Frontend (Next.js)
        ↓
REST APIs
        ↓
Django Backend
        ↓
SQLite Database
```

---

# Modules in the Project

## 1. Authentication Module

This module handles user authentication and security.

### Features

* User Registration
* User Login
* JWT Authentication
* Google Login Integration
* Protected Routes
* Logout Functionality

### Description

Users can create accounts and securely log in to the system. JWT tokens are used for authentication and route protection.

Google OAuth was integrated to allow users to log in using their Google accounts.

---

## 2. Task Management Module

This module manages all task-related operations.

### Features

* Create Task
* Edit Task
* Delete Task
* Mark Task as Completed
* Update Task Status
* Due Date Management
* Priority Management

### Description

Users can create tasks with:

* Title
* Description
* Priority
* Due Date

Tasks can later be updated or deleted. Users can also mark tasks as completed or pending.

---

## 3. Search and Filter Module

### Features

* Search Tasks
* Filter by Priority
* Filter by Status

### Description

This module helps users quickly find tasks using search functionality and priority filters.

---

## 4. SMTP Email Notification Module

### Features

* Email notifications on task creation
* SMTP integration using Gmail

### Description

Whenever a new task is created, the system automatically sends an email notification to the user.

SMTP was implemented using Django Email Services and Gmail SMTP configuration.

---

## 5. Admin Dashboard Module

### Features

* Separate custom admin panel
* View all users
* View all tasks
* Task statistics
* Pending tasks count
* Completed tasks count
* High priority task count

### Description

A separate admin dashboard was implemented using Next.js instead of Django Admin.

This dashboard allows administrators to monitor:

* User activity
* Task statistics
* Overall system performance

---

# Frontend Features

## Dashboard Features

* Dark Mode
* Task Statistics
* Responsive Design
* Search Bar
* Priority Filters
* Task Cards
* Admin Navigation Button

## UI Design

The frontend was designed using Tailwind CSS to provide:

* Clean user interface
* Responsive layouts
* Modern design
* Better user experience

---

# Backend Features

## API Features

* REST APIs
* JWT Protected Endpoints
* CRUD APIs
* Search APIs
* Status Update APIs
* File Upload APIs

## Security Features

* Token-based authentication
* Protected routes
* User-specific task access

---

# Database Design

## Main Tables

### User Table

Stores:

* Username
* Email
* Password
* Role

### Task Table

Stores:

* Task Title
* Description
* Priority
* Status
* Due Date
* Created By

### Task Comment Table

Stores comments related to tasks.

### Task Attachment Table

Stores uploaded files.

---

# Authentication Flow

```text
User Login
     ↓
JWT Token Generated
     ↓
Token Stored in Frontend
     ↓
Protected API Access
```

---

# SMTP Workflow

```text
Create Task
     ↓
Task Saved in Database
     ↓
SMTP Triggered
     ↓
Email Sent to User
```

---

# Admin Dashboard Workflow

```text
Admin Login
      ↓
Admin Dashboard Access
      ↓
View Users and Tasks
      ↓
Monitor Task Statistics
```

---

# Project Folder Structure

```text
frontend/
 ├── src/
 │    ├── app/
 │    ├── components/
 │    ├── services/
 │    └── styles/

backend/
 ├── apps/
 │    ├── authentication/
 │    ├── tasks/
 │    ├── users/
 │    └── teams/
 ├── config/
 └── manage.py
```

---

# Components Architecture

Reusable components were implemented for better scalability and metadata support.

### Components Created

* Login Component
* Register Component
* Dashboard Component
* Admin Dashboard Component

This architecture improves:

* Code reusability
* Maintainability
* Scalability
* Metadata support

---

# API Endpoints

## Authentication APIs

* Register API
* Login API
* Google Login API

## Task APIs

* Create Task
* Update Task
* Delete Task
* Search Tasks
* Update Task Status

## Admin APIs

* Dashboard Statistics
* All Users API

---

# Challenges Faced

Some challenges faced during development include:

* Frontend and backend integration
* JWT authentication setup
* Google OAuth integration
* SMTP configuration
* Role-based admin dashboard implementation
* API debugging

These issues were resolved through testing and API integration improvements.

---

# Future Enhancements

Future improvements that can be added:

* Task reminders
* Team collaboration
* Real-time notifications
* Mobile application
* Advanced analytics
* Calendar integration

---

# Conclusion

The Task Manager System successfully provides a secure and user-friendly platform for managing tasks.

The project includes:

* Secure authentication
* Task management
* Email notifications
* Admin monitoring dashboard
* Responsive frontend
* REST API architecture

This system improves task organization, productivity, and monitoring while following modern full-stack development practices.

---

# Installation and Setup Guide

## Backend Setup

### Step 1: Navigate to Backend Folder

```bash
cd backend
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Start Backend Server

```bash
python manage.py runserver
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

### Step 1: Navigate to Frontend Folder

```bash
cd frontend
```

### Step 2: Install Node Modules

```bash
npm install
```

### Step 3: Start Frontend Server

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# Localhost Execution

To run the complete project locally:

## Start Backend

```bash
cd backend
python manage.py runserver
```

## Start Frontend

```bash
cd frontend
npm run dev
```

Then open:

```text
http://localhost:3000
```

in the browser.

The frontend communicates with the Django backend APIs running on localhost.

---

# Developed By

Venkateswarlu Vennampalli



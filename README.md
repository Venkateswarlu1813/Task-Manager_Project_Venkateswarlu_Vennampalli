# Full Stack Task Manager Application

A modern Full Stack Task Management System built using **Next.js**, **Django REST Framework**, and **JWT Authentication** with features like task creation, editing, status management, Google Login, due dates, filtering, and responsive UI.

---

# 📌 Features

## 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- Google OAuth Login
- Secure Protected Routes
- Logout Functionality

---

## 📋 Task Management
- Create Tasks
- Edit Tasks
- Delete Tasks
- Mark Tasks as Complete / Pending
- Task Status Toggle
- Task Priority Levels
  - High
  - Medium
  - Low
- Due Date Support
- Task Description Support

---

## 🎯 Dashboard Features
- Dashboard Statistics
- Total Tasks Counter
- Completed Tasks Counter
- Pending Tasks Counter
- High Priority Tasks Counter
- Animated UI Cards
- Responsive Dashboard Layout

---

## 🔎 Filtering & Search
- Filter Tasks by Priority
- Filter Tasks by Status
- Dynamic Task Display

---

## 🌙 UI/UX Features
- Dark / Light Theme Toggle
- Responsive Design
- Modern UI with Tailwind CSS
- Toast Notifications
- Interactive Task Cards
- Expandable Task Details

---

# 🛠️ Tech Stack

## Frontend
- Next.js
- React.js
- Tailwind CSS
- Axios
- React Hot Toast

## Backend
- Django
- Django REST Framework
- JWT Authentication
- Google OAuth
- SQLite

---

# 📂 Project Structure

```bash
Task_Manager_Project/
│
├── backend/
│   ├── apps/
│   ├── config/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── next.config.mjs
│   ├── postcss.config.mjs
│   ├── eslint.config.mjs
│   └── jsconfig.json
│
├── .gitignore
└── README.md

⚙️ Installation & Setup
Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Frontend Setup
cd frontend
npm install
npm run dev

🔑 Environment Variables
Frontend (.env.local)
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
NEXT_PUBLIC_GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID
Backend (.env)
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=True

📡 API Endpoints
Authentication
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/google/

Tasks
GET /api/tasks/
POST /api/tasks/
PUT /api/tasks/{id}/
DELETE /api/tasks/{id}/
PATCH /api/tasks/status/{task_id}/

✨ Advanced Features Added
Google OAuth Authentication
Task Completion Toggle
Due Date Management
Task Editing
Task Filtering
Dynamic Dashboard Stats
Toast Notifications
Protected Routes
Modern Responsive UI

👨‍💻 Developed By
Venkateswarlu Vennampalli

📌 Future Enhancements
Team Collaboration
File Attachments
Task Comments
Email Notifications
Drag & Drop Kanban Board
Real-time Updates

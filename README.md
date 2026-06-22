# Full Stack Job Portal Application

A modern Full Stack Job Portal built with FastAPI, React, TypeScript, SQLite, and JWT Authentication.

## Features

* User Registration & Login
* JWT Authentication
* Browse Available Jobs
* View Job Details
* Apply for Jobs
* Track My Applications
* Responsive React Frontend
* FastAPI REST API Backend
* SQLite Database Integration

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* CSS

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Pydantic

## Project Structure

```text
Full Stack Job Portal Application
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   ├── app.db
│   └── seed_internships.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
└── render.yaml
```

## Installation

### Backend Setup

```bash
cd backend

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

Open another terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

(or the next available port)

## API Endpoints

### Authentication

* POST /api/auth/register
* POST /api/auth/login

### Jobs

* GET /api/jobs
* GET /api/jobs/{job_id}
* POST /api/jobs

### Applications

* POST /api/applications
* GET /api/applications/mine

## Database

The application uses SQLite for development.

Database file:

```text
backend/app.db
```

Sample internship data can be inserted using:

```bash
python seed_internships.py
```

## Deployment

### Backend

* Render
* Railway

### Frontend

* Netlify
* Vercel
* Render Static Site

## Screenshots

Add screenshots here after deployment.

### Home Page

![Home Page](screenshots/home.png)

### Job Listings

![Jobs](screenshots/jobs.png)

### Apply Job

![Apply](screenshots/apply.png)

## Future Enhancements

* Resume Upload
* Admin Dashboard
* Company Profiles
* Email Notifications
* PostgreSQL Support
* Advanced Job Search & Filters

## Author

Gangadhar Reddy

GitHub:
https://github.com/gangadharreddy065-create

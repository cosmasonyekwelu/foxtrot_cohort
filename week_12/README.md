# Deploying the Bank Application API to Render

This document provides a complete, production-ready guide for deploying the **Django + Django REST Framework + JWT Bank Application API** to **Render**.
It reflects the exact setup, tools, and decisions used in this project.

---

## 1. Pre-Deployment Checklist (Local Setup)

Before deploying to Render, ensure the project is correctly prepared locally.

---

### 1.1 Requirements File

Generate or update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Confirm the file includes the following dependencies:

- django
- djangorestframework
- djangorestframework-simplejwt
- drf-spectacular
- drf-spectacular-sidecar
- gunicorn
- psycopg2-binary
- dj-database-url
- python-dotenv (for local development)

---

### 1.2 Production Settings Adjustments

In `settings.py`:

#### Disable Debug Mode

```python
DEBUG = False
```

#### Allowed Hosts (Temporary)

```python
ALLOWED_HOSTS = ["*"]  # restrict after deployment
```

This will later be replaced with your Render domain.

---

### 1.3 Static Files Configuration

Add the following to `settings.py`:

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Run locally once to verify:

```bash
python manage.py collectstatic
```

---

## 2. Database Configuration (Critical)

### 2.1 Switching from SQLite to PostgreSQL

SQLite is not suitable for production on Render.

Install the PostgreSQL driver:

```bash
pip install psycopg2-binary
```

Update `settings.py`:

```python
import dj_database_url
import os

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}
```

Ensure `dj-database-url` is present in `requirements.txt`.

---

## 3. Environment Variables Configuration

### 3.1 Local Environment (`.env`)

Create a `.env` file at the project root (same level as `manage.py`):

```env
DEBUG=True
SECRET_KEY=django-insecure-local-secret
DATABASE_URL=sqlite:///db.sqlite3
```

Add `.env` to `.gitignore`:

```
.env
```

Load it in `settings.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

### 3.2 Render Environment Variables (Production)

Render does **not** use `.env` files.
All environment variables must be added via the dashboard.

In **Render → Web Service → Environment**, add:

| Key           | Value                      |
| ------------- | -------------------------- |
| SECRET_KEY    | Django secret key          |
| DATABASE_URL  | PostgreSQL Internal URL    |
| DEBUG         | False                      |
| ALLOWED_HOSTS | your-app-name.onrender.com |

---

## 4. Procfile Setup (Required)

Render needs a process definition to start your Django app.

### 4.1 Create a Procfile

At the **project root**, create a file named:

```
Procfile
```

Content:

```procfile
web: gunicorn mibank.wsgi
```

Explanation:

- `web:` declares a web service
- `gunicorn` is the production WSGI server
- `mibank.wsgi` points to your Django app

Ensure `gunicorn` is installed and listed in `requirements.txt`.

---

## 5. Version Control (GitHub)

Render deploys directly from GitHub.

Commit all deployment-related changes:

```bash
git add .
git commit -m "Prepare Django API for Render deployment"
git push origin main
```

---

## 6. Render Deployment Process

### 6.1 Create a PostgreSQL Database

1. Go to Render Dashboard
2. Click **New → PostgreSQL**
3. Name it (example: `mibank-db`)
4. Create database
5. Copy the **Internal Database URL**

---

### 6.2 Create the Web Service

1. Click **New → Web Service**
2. Connect your GitHub repository
3. Select branch (`main`)
4. Runtime: **Python**
5. Build Command:

```
pip install -r requirements.txt
```

6. Start Command:

```
gunicorn mibank.wsgi:application
```

7. Save and deploy

---

## 7. Running Migrations on Render

After the first successful deploy:

1. Open **Render Shell**
2. Run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

This creates all required tables:

- Users
- Accounts
- Transactions
- LoanApplications

---

## 8. Verifying Deployment

Once deployment completes, verify the following:

### Base URL

```
https://your-app-name.onrender.com/
```

### Swagger Documentation

```
https://your-app-name.onrender.com/api/docs/swagger/
```

### Login Endpoint Test

```
POST /auth/login/
```

Expected response includes JWT access and refresh tokens.

---

## 9. Post-Deployment Checklist

Confirm:

- Admin panel loads correctly
- Migrations applied successfully
- JWT authentication works
- Loan permissions work (current accounts only)
- Swagger UI renders correctly

---

## 10. Common Deployment Issues and Fixes

| Issue                | Cause                 | Solution             |
| -------------------- | --------------------- | -------------------- |
| DisallowedHost error | ALLOWED_HOSTS not set | Add Render domain    |
| Database errors      | SQLite used           | Switch to PostgreSQL |
| Static files missing | collectstatic not run | Run collectstatic    |
| App crashes on boot  | gunicorn missing      | Install gunicorn     |
| 500 errors           | DEBUG=False           | Check Render logs    |

---

## 11. Recommended Next Steps

After deployment:

1. Restrict `ALLOWED_HOSTS` properly
2. Hide Swagger in production (optional)
3. Enable logging
4. Add automated tests
5. Add rate limiting for auth endpoints

---

## 12. Summary

This deployment setup ensures:

- Secure secret management
- Production-grade WSGI server
- PostgreSQL-backed persistence
- Proper static file handling
- Scalable and maintainable hosting on Render

---

# Week 9: Day 1. Bank Application API (Django + DRF + JWT)

This document contains the full setup, configuration, and foundational work for creating a Bank Application API using Django, Django REST Framework, a custom User model, and SimpleJWT authentication.

The API will support secure authentication and serve as the foundation for banking operations such as account management, transactions, deposits, withdrawals, and transfers.

---

## 1. Project Setup

### Create and activate virtual environment

```bash
py -m venv venv
venv\Scripts\activate
```

### Install Django

```bash
pip install django
```

### Start a new Django project

```bash
django-admin startproject mibank .
```

### Create the users app

```bash
py manage.py startapp users
```

### Freeze installed packages

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file for reproducible installation later.

---

## 2. Custom User Manager

Create a file `users/managers.py` and add the custom manager:

```python
from django.contrib.auth.models import BaseUserManager

class Manager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)
```

This manager replaces Django’s default username-based authentication with an email-based system.

---

## 3. Custom User Model

Create or update `users/models.py`:

```python
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator
from .managers import Manager

class User(AbstractUser, PermissionsMixin):
    ACCOUNT_TYPE_CHOICES = (
        ("current", "Current"),
        ("savings", "Savings"),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    username = None

    bvn = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        unique=True
    )

    nin = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        unique=True
    )

    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)

    account_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True
    )

    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)

    amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = Manager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Users"
```

Important notes:

- `AbstractUser` is extended but the `username` field is disabled.
- Authentication is based solely on the `email` field.
- BVN, NIN, and account_number enforce fixed length and uniqueness.
- PermissionsMixin ensures superuser and staff permissions still work.

---

## 4. Register User Model in Django Admin

Add this to `users/admin.py`:

```python
from django.contrib import admin
from .models import User

admin.site.register(User)
```

---

## 5. Update Django Settings

Open `mibank/settings.py` and configure the custom user model:

```python
AUTH_USER_MODEL = "users.User"
```

### Add installed apps:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "users",
    "rest_framework",
    "rest_framework_simplejwt",
]
```

---

## 6. Install and Configure SimpleJWT

### Install djangorestframework-simplejwt

```bash
pip install djangorestframework-simplejwt
```

---

## 7. Configure Django REST Framework

Add this block to `settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ]
}
```

This enforces JWT authentication on all API endpoints by default.

---

## 8. Correct SimpleJWT Configuration

Insert inside `settings.py`:

```python
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,

    "AUTH_HEADER_TYPES": ("Bearer",),
}
```

This defines:

- Access token valid for 24 hours
- Refresh token valid for 7 days
- Uses HS256 signing with project SECRET_KEY
- JWT tokens are sent using `Authorization: Bearer <token>`

---

## 9. Add JWT Authentication URLs

Edit the main URL file `mibank/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```

### Example: Obtain token (login)

Send a POST request to `/api/token/`:

```json
{
  "email": "admin@example.com",
  "password": "adminpassword"
}
```

### Example: Refresh token

Send POST to `/api/token/refresh/`:

```json
{
  "refresh": "your_refresh_token_here"
}
```

---

## 10. Apply Migrations

Run:

```bash
py manage.py makemigrations
py manage.py migrate
```

---

## 11. Create a Superuser

Because the username field is removed, Django will ask only for an email and password.

```bash
py manage.py createsuperuser
```

---

## Summary

By completing these steps, the following were fully configured:

1. Django project and environment setup
2. Custom email-based user model
3. Custom user manager
4. JWT authentication for all API routes
5. DRF authentication and permission defaults
6. JWT login and refresh endpoints
7. Database migrations and admin integration

At this point, the project is ready for Day 2 tasks:

- User registration endpoint
- User login endpoint connected to SimpleJWT
- Bank account and transaction models
- Deposit, withdrawal, and transfer logic
- API security and permissions

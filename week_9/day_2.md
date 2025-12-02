Below is a **rewritten, improved, production-friendly, step-by-step documentation** for *Week 9 – Day 2*, **including package installation guides**, explanations of why each package is needed, and a complete walkthrough of how the authentication system works.

---

# Week 9 – Day 2

## Building a Secure Bank Application API

### Using Django, Django REST Framework, and JWT Authentication

This lesson focused on implementing a **secure authentication system** using:

* Django
* Django REST Framework (DRF)
* SimpleJWT (JSON Web Tokens)

We built **user registration and login APIs**, created a custom serializer, and learned how to validate and serialize incoming data.

---

# 1. Environment Setup & Package Installation

Before writing any authentication code, we installed the core backend packages.

## 1.1 Install Required Packages

Run:

```bash
pip install Django djangorestframework djangorestframework-simplejwt 
```

### What each package does:

| Package                           | Purpose                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Django**                        | The main web framework used to build the API. Handles models, migrations, routing, and admin panel.                     |
| **djangorestframework (DRF)**     | Adds API-building tools like serializers, viewsets, permissions, parsing, pagination, etc. Required to build REST APIs. |
| **djangorestframework-simplejwt** | Implements JWT (access & refresh tokens). Used for login and protected routes.                                          |


---

# 2. Creating the Authentication Endpoints

We built two API routes using `@api_view`:

* `/register/` — Create a new user
* `/login/` — Authenticate user and return JWT tokens

These views rely on a **RegisterSerializer** that handles all validation and user creation.

---

# 3. Register API (Signup Endpoint)

## What it does:

* Accepts incoming user data
* Uses `RegisterSerializer` for validation
* Creates a new user
* Returns success or validation errors

Key points:

* Anyone can access this endpoint (`AllowAny`)
* Passwords are hashed using `set_password()`
* Serializer ensures email, BVN, NIN, account type, etc., are validated

---

# 4. Login API (JWT Authentication)

## What login does:

* Validates email + password using Django's `authenticate()`
* If correct → generates JWT `access` and `refresh` tokens
* Returns tokens to the frontend
* If incorrect → returns authentication error

### What SimpleJWT provides:

* **Access Token** → used for authenticated API calls
* **Refresh Token** → used to get new access tokens without logging in

JWT ensures **stateless authentication**, which is required for modern mobile/web apps.

---

# 5. RegisterSerializer (Core of Signup Logic)

The `RegisterSerializer` performs:

## ✔ Input validation

Ensures fields like:

* email
* password
* nin
* bvn
* account_type

are correctly formatted.

### ✔ Password validation

Uses Django's built-in password validators.

### ✔ Secure password hashing

Uses:

```python
user.set_password(password)
```

Passwords are never stored in plain text.

### ✔ Data serialization

Controls what is returned to Postman / frontend.

---

# 6. Serialization Explained

## Serialization

Convert Python object → JSON response

Example:

```python
User → {"email": "john@example.com"}
```

### Deserialization

Convert incoming JSON → Python data structure Django can use

Example:

```json
{
  "email": "john@example.com",
  "password": "Pass1234!"
}
```

DRF deserializes this into Python data and validates it before saving.

In summary:

| Direction     | Meaning         |
| ------------- | --------------- |
| Python → JSON | Serialization   |
| JSON → Python | Deserialization |

---

# 7. Project Structure (Simplified)

```
users/
    models.py
    views.py
    serializers.py
    urls.py
project/
    settings.py
    urls.py
```

* `models.py` → User database structure
* `serializers.py` → Validates inputs, creates users
* `views.py` → Register/Login logic
* `urls.py` → Route definitions

---

# 8. Authentication API Flow

## A. Register

```
POST /register/
```

Process:

1. Validate input
2. Create user
3. Hash password
4. Return success JSON

---

## B. Login

```
POST /login/
```

Process:

1. Validate email + password
2. Authenticate user
3. Issue JWT access & refresh tokens
4. Return tokens to frontend

Tokens are used to call **protected endpoints**.

---

# 9. Summary

By the end of Week 9 Day 2, we learned how to:

* Install and configure Django + DRF
* Add JWT authentication using SimpleJWT
* Create custom serializers for secure user creation
* Build register and login API endpoints
* Understand serialization & deserialization clearly
* Handle validation and error reporting correctly



---


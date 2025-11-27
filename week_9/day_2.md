# Week 9: Day 2

## Bank Application API (Django + DRF + JWT)

This session covered how to implement **user registration and login** using **Django REST Framework** along with **JWT authentication** provided by `rest_framework_simplejwt`.

We also created a custom `RegisterSerializer` to handle user creation, password validation, and proper serialization of incoming data.

---

## Key Topics Covered

### 1. Django REST API Views

We created two main API endpoints using the `@api_view` decorator:

#### a. Register Endpoint

Allows anyone to create an account.
Key points:

* Uses `RegisterSerializer`
* Validates input
* Saves a new user
* Returns a success message or validation errors

#### b. Login Endpoint

Authenticates a user by email and password.
If authentication is successful:

* Generates an `access` token
* Generates a `refresh` token
* Returns both tokens in the response

If authentication fails:

* Returns an error message

---

## 2. JWT Authentication (SimpleJWT)

We used:

* `AccessToken.for_user(user)`
* `RefreshToken.for_user(user)`

The **access token** is used for short-lived authenticated requests.
The **refresh token** allows generating a new access token without logging in again.

---

## 3. RegisterSerializer

The `RegisterSerializer` handles:

* Validating incoming user data
* Validating password strength using Django's built-in validators
* Creating the user object
* Hashing the password using `set_password`

Fields like `account_number`, `account_type`, `bvn`, and `nin` were set as optional.

---

## Code Summary

### Registration View

Handles user signup.

### Login View

Authenticates the user and issues JWT tokens.

### RegisterSerializer

Ensures data is properly validated and creates a secure user object.

---

# Serialization and Deserialization Explained 

## Serialization

Serialization means **converting Python objects into JSON** so they can be sent through the API.

Example:
You have a `User` object in the database.
Serialization converts it to JSON like:

```
{
  "first_name": "John",
  "email": "john@example.com"
}
```

### Deserialization

Deserialization means **converting JSON received from the client into Python objects** so Django can work with them.

Example:
You send this JSON to the API:

```
{
  "first_name": "John",
  "email": "john@example.com",
  "password": "Pass1234!"
}
```

DRF deserializes it into Python data, validates it, and uses it to create a `User` object.

In summary:

* Serialization: Python → JSON
* Deserialization: JSON → Python

---

# Project Structure (Simplified)

```
views.py
serializers.py
models.py
urls.py
```

* `views.py` contains the register and login logic.
* `serializers.py` validates user data and creates users.
* `models.py` stores the custom User model.
* `urls.py` maps the API routes.

---

# How the API Works

## Register

POST `/register/`

* Validates data
* Saves user
* Returns success message

### Login

POST `/login/`

* Verifies email and password
* Issues access and refresh tokens
* Returns authentication details

---


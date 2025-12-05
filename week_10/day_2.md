# Bank Application API — Day 2 Documentation

This documentation explains what was achieved on **Day 2** of building the Bank Application API, focusing on database modeling, serializers, view logic, routing, and backend testing using Postman. It also includes the key problems faced and solutions applied.

---

## Topics Covered on Day 2

1. Setting up the `accounts` app
2. Understanding model relationships in Django
3. Implementing the One-to-One model relationship
4. Writing the `Accounts` model
5. Creating the serializer for validation and saving data
6. Implementing API endpoints to create and delete accounts
7. Testing endpoints with Postman
8. Debugging and resolving migration/database errors

---

## Model Relationships Explained

A **model relationship** describes how two database tables are connected.

### 1. One-to-One Relationship

- Each record in one table maps to exactly one record in another.
- Use case:

  - One user → One account (bank system use case)

- Django implementation:

  ```python
  user = models.OneToOneField(User)
  ```

### 2. One-to-Many Relationship

- A single record relates to multiple records in another table.
- Use case:

  - One customer → Many transactions

- Django implementation:

  ```python
  user = models.ForeignKey(User)
  ```

### 3. Many-to-Many Relationship

- Multiple items from table A relate to multiple items from table B.
- Use case:

  - Users and roles (e.g., admin, staff, accountant)

- Django implementation:

  ```python
  users = models.ManyToManyField(User)
  ```

---

## Why One-to-One for Our Accounts App?

- Each user should have **only one** bank account.
- Prevents multiple accounts being linked to the same user.
- Ensures database integrity and enforces business logic.

---

## Accounts Model (accounts/models.py)

```python
from django.db import models

class Accounts(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ("current", "Current"),
        ("savings", "Savings"),
    )

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_account",
        null=True,
        blank=True
    )
    bvn = models.CharField(max_length=11)
    nin = models.CharField(max_length=11)
    account_number = models.CharField(max_length=10, null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Account: {self.account_number}"
```

---

## Serializer (accounts/serializers.py)

```python
from rest_framework import serializers
from .models import Accounts
import random

class CreateAccount(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = "__all__"

    def validate(self, incoming_data):
        if len(incoming_data["bvn"]) != 11:
            raise serializers.ValidationError("BVN must be 11 digits")
        if len(incoming_data["nin"]) != 11:
            raise serializers.ValidationError("NIN must be 11 digits")
        return incoming_data

    def create(self, validated_data, **kwargs):
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])

        account = Accounts(
            user=validated_data["user"],
            bvn=validated_data["bvn"],
            nin=validated_data["nin"],
            account_type=validated_data["account_type"],
            account_number=account_number
        )

        account.save()
        return account
```

---

## Views for Account Endpoints (accounts/views.py)

```python
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from accounts import serializers
from users.models import User

@api_view(["POST"])
def create_account(request):
    user = request.user.id
    account_data = request.data.copy()
    account_data['user'] = user

    serializer = serializers.CreateAccount(data=account_data)
    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response({"message": "Your account has been created"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_account(request):
    user_id = request.user.id
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

---

## URL Configuration (accounts/urls.py)

```python
from django.urls import path
from accounts import views

urlpatterns = [
    path("create/", views.create_account, name="create_account"),
    path("delete/", views.delete_account, name="delete_account")
]
```

---

## Database Migrations

To apply model changes:

```bash
py manage.py makemigrations
py manage.py migrate
```

---

## Testing with Postman

### 1. Creating an Account (POST)

**Endpoint:**

```
POST /accounts/create/
```

**Headers:**

```
Authorization: Bearer <valid access token>
Content-Type: application/json
```

**Body Example:**

```json
{
  "bvn": "12345678901",
  "nin": "98765432109",
  "account_type": "current"
}
```

**Expected Response:**

```json
{
  "message": "Your account has been created"
}
```

---

### 2. Deleting an Account (DELETE)

**Endpoint:**

```
DELETE /accounts/delete/
```

**Headers:**

```
Authorization: Bearer <valid access token>
```

**Expected Response on Success:**

```json
{}
```

**Expected Status Code:**

```
204 No Content
```

**If User Doesn’t Exist:**

```json
{
  "message": "User not found"
}
```

---

## Errors and Solutions

### Issue 1:

```
no such column: accounts_accounts.user_id
```

**Reason:** Model changed; database didn’t update.

**Fix:**

- Delete migrations and db
- Re-run migrations

---

### Issue 2:

```
KeyError: 'user'
```

**Reason:** Serializer attempted to access user inside validated_data.

**Fix:** Ensure user is injected into request data.

---

## Key Points Learned

- One-to-One relationship use case
- Importance of serializer validation logic
- Why auto-generated fields (like account number) are handled in `create()`
- Proper use of POST and DELETE endpoints
- Handling authenticated user requests
- Resolving migration inconsistencies

---



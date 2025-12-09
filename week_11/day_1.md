# Bank Application API – Comprehensive Documentation (Week 11 – Day 1)

This backend API simulates real-world banking operations, including user authentication, account creation, secure deposits and transfers, and transaction logging.
It leverages Django, Django REST Framework, and JWT authentication.

---

## 1. Apps Included in This Project

### 1.1 Users App

Handles:

- Registration
- Login (JWT)
- Profile update

Files created:

- users/models.py
- users/serializers.py
- users/views.py
- users/urls.py

---

### 1.2 Accounts App

Handles:

- Account creation
- Linking users to accounts (1-to-1)
- BVN/NIN validation
- Balance tracking

Files created:

- accounts/models.py
- accounts/serializers.py
- accounts/views.py
- accounts/urls.py

---

### 1.3 Transactions App

Handles:

- Deposits
- Transfers
- Transaction recording
- Sender and receiver referencing same table

Files created:

- transactions/models.py
- transactions/serializers.py
- transactions/views.py
- transactions/urls.py

---

## 2. Concepts Learned and Implemented Properly

### 2.1 Atomic Transactions

Bank operations must not partially update.
If two database updates occur, they must both complete successfully or both be rolled back.

Example used:

```python
with transaction.atomic():
    sender.amount -= float(amount)
    sender.save()
    receiver.amount += float(amount)
    receiver.save()
```

---

### 2.2 Self-Referential Model Relationships

The `Transactions` model references `Accounts` twice:

```python
sender = models.ForeignKey('accounts.Accounts', ...)
receiver = models.ForeignKey('accounts.Accounts', ...)
```

This allows:

- Deposit: sender == receiver
- Transfers between two accounts

---

### 2.3 One-to-One User to Account Relationship

One user can only own one account:

```python
user = models.OneToOneField("users.User", related_name="user_account")
```

---

## 3. Database Models

### 3.1 Users Model

Users store personal information and password securely.

### 3.2 Accounts Model

Tracks financial information:

```python
amount = models.FloatField(default=0.0)
account_number = models.CharField(max_length=10)
```

### 3.3 Transactions Model

Stores all movements:

- sender account
- receiver account
- amount
- status ("success")
- description

---

## 4. Serializers

### 4.1 User Serializers

Used for registration and updates.

### 4.2 Account Serializers

Includes validation for BVN and NIN.

### 4.3 Transaction Serializers

Stores transaction history.

---

## 5. Routes Overview

---

### 5.1 User Routes

#### A. Register User

```
POST /auth/register/
```

Request:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone_number": "0909998888",
  "password": "StrongPass123!"
}
```

Response:

```json
{
  "message": "User registered successfully"
}
```

---

#### B. Login User

```
POST /auth/login/
```

Request:

```json
{
  "email": "john@example.com",
  "password": "StrongPass123!"
}
```

Response:

```json
{
  "message": "User Login successful",
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

---

#### C. Update User Information

```
PATCH /auth/update/
```

Request:

```json
{
  "first_name": "Johnny",
  "date_of_birth": "2000-7-7"
}
```

Response:

```json
{
  "message": "User details updated successfully"
}
```

---

### 5.2 Account Routes

#### A. Create Account

```
POST /accounts/create/
```

Request:

```json
{
  "bvn": "12345678901",
  "nin": "33445566778",
  "account_type": "savings"
}
```

Response:

```json
{
  "message": "Account created successfully"
}
```

---

#### B. View Account Details

```
GET /accounts/details/
```

Response:

```json
{
  "user": {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone_number": "0909998888"
  },
  "account_number": "1029384756",
  "account_type": "savings",
  "amount": 5000.0
}
```

---

### 5.3 Transaction Routes

#### A. Deposit

```
POST /transactions/deposit/
```

Request:

```json
{
  "amount": 3000
}
```

Operations:

- Account balance increases
- Transaction recorded as self-transfer

Response:

```json
{
  "message": "Deposit successful"
}
```

---

#### B. Transfer

```
POST /transactions/transfer/
```

Request:

```json
{
  "account_number": "2233445566",
  "amount": 2000
}
```

Operations:

- Sender balance decreases
- Receiver balance increases
- Transaction recorded

Response:

```json
{
  "message": "Transfer successful",
  "sender": "1029384756",
  "receiver": "2233445566",
  "amount": 2000.0
}
```

---

## 6. Migration and Error Handling Summary

| Issue                                      | Cause                                            | Fix                                     |
| ------------------------------------------ | ------------------------------------------------ | --------------------------------------- |
| `no such table: transactions_transactions` | Migrations not applied                           | Ran `makemigrations` + `migrate`        |
| Wrong lookup on account                    | Used `request.user.id` instead of `request.user` | Corrected                               |
| Transaction amounts incorrect              | Used total balance instead of incoming amount    | Corrected                               |
| Data not saved                             | Serializer invalid                               | Added `.is_valid(raise_exception=True)` |
| Balance not updating properly              | Non-atomic updates                               | Wrapped in `transaction.atomic()`       |

---

## 7. What We Achieved Today

- Built banking-grade data models
- Implemented dynamic validation
- Corrected migration handling
- Implemented atomic money movements
- Implemented self-referential financial transactions
- Improved serializer usage
- Built clean, reusable modular code
- Learned real-world financial backend design concepts

---

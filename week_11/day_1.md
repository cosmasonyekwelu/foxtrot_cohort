# Bank Application API – Comprehensive Documentation for week 11 day One

This backend is built with Django REST Framework and JWT authentication. It simulates real-world banking operations such as creating accounts, viewing account details, depositing funds, transferring money, and logging all transactions.

---

## 1. Features Implemented

- User registration and authentication (JWT)
- Account creation linked to users
- BVN and NIN validation
- Auto-generated 10-digit account numbers
- Deposits and transfers between accounts
- Transaction logging (sender and receiver)
- Atomic operations preventing partial database changes
- Self-referential model relationships for transactions

---

## 2. Core Terminology Explained

### 2.1 Atomic Transactions

Atomic transactions ensure that multiple related database operations complete entirely or not at all. This prevents situations such as:

- Deducting money from sender but failing to credit receiver
- Deposit amount updating but no transaction logged

We used:

```python
with transaction.atomic():
```

Example in transfer logic:

```python
def transfer_money(sender, receiver, amount):
    with transaction.atomic():
        sender.amount -= float(amount)
        sender.save()

        receiver.amount += float(amount)
        receiver.save()
```

If anything inside fails, everything inside is rolled back.

---

### 2.2 Self-Referential Model Relationships

A self-referential relationship means a model references itself.
The transaction model holds:

- sender (Account)
- receiver (Account)

Both point to the same table, Accounts.

Used here:

```python
class Transactions(models.Model):
    sender = models.ForeignKey('accounts.Accounts', ...)
    receiver = models.ForeignKey('accounts.Accounts', ...)
```

This allowed:

- Deposit logged as sender = receiver
- Transfers logged between accounts

---

### 2.3 One-to-One User to Account Relationship

Each user has exactly one account.

```python
user = models.OneToOneField(
    "users.User",
    related_name="user_account"
)
```

---

## 3. Database Structure Overview

### Accounts Model

- Linked to user
- BVN, NIN validation
- Auto-generated account number
- Balance tracking

### Transaction Model

- Links sender and receiver
- Stores description and status
- Useful for history, disputes, reversals

---

## 4. API Routes

---

### 4.1 User Routes

#### A. Register User

```
POST /auth/register/
```

##### Sample Request

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone_number": "0909998888",
  "password": "StrongPass123!"
}
```

##### Expected Response:

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

##### Sample Request

```json
{
  "email": "john@example.com",
  "password": "StrongPass123!"
}
```

##### Expected Response:

```json
{
  "message": "User Login successful",
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

---

#### C. Update User Profile

```
PATCH /auth/update/
```

##### Sample Request

```json
{
  "first_name": "Johnny",
  "date_of_birth": "2000-7-7"
}
```

##### Expected Response

```json
{
  "message": "User details updated successfully"
}
```

---

## 4.2 Account Routes

---

### A. Create Account

```
POST /accounts/create/
```

#### Sample Request

```json
{
  "bvn": "12345678901",
  "nin": "33445566778",
  "account_type": "savings"
}
```

##### Expected Response

```json
{
  "message": "Account created successfully"
}
```

---

### B. View Account Details

```
GET /accounts/details/
```

#### Expected Response

```json
{
  "user": {
    "id": 1,
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

## 4.3 Transaction Routes

---

### A. Deposit

```
POST /transactions/deposit/
```

#### Sample Request:

```json
{
  "amount": 3000
}
```

##### Behavior:

- User balance increases by 3000
- A transaction is created (sender == receiver)

##### Expected Response:

```json
{
  "message": "Deposit successful"
}
```

---

### B. Transfer

```
POST /transactions/transfer/
```

#### Sample Request:

```json
{
  "account_number": "2233445566",
  "amount": 2000
}
```

##### Behavior:

- Sender amount decreases
- Receiver amount increases
- Transaction created linking both

##### Expected Response:

```json
{
  "message": "Transfer successful",
  "sender": "1029384756",
  "receiver": "2233445566",
  "amount": 2000.0
}
```

---

## 5. Errors Faced and Solutions

| Issue                          | Cause                                          | Solution                                       |
| ------------------------------ | ---------------------------------------------- | ---------------------------------------------- |
| Migration errors               | Model added but no migration executed          | Ran `makemigrations` and `migrate`             |
| "No such table"                | DB schema outdated                             | Reapplied migrations                           |
| BVN/NIN invalid                | Wrong length input                             | Added validation in serializer                 |
| Transaction saved wrong values | Used account.amount instead of incoming amount | Corrected serializer data                      |
| Account not found              | Wrong lookup                                   | Used `Accounts.objects.get(user=request.user)` |

---

## 6. Things Learned

### Validations

You validated BVN and NIN lengths.

### Atomic Database Operations

Used to protect financial consistency.

### Self-Referential Relationships

Allowed sender and receiver to be stored in one model.

### DRF Serialization

You used serializers both for input validation and object creation.

### JWT Authentication

Used to secure all financial routes.

---

This README captures all that we tested, debugged, and improved today.

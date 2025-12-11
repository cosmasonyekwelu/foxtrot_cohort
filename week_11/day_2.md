# Bank Application API – Comprehensive Documentation (Week 11 – Day 2)

This document covers all development activities completed on Week 11, Day 2 of the Bank Application API project.
Today’s work focused on API documentation (Swagger), loan application logic, custom permissions, Django admin setup, URL structuring, and testing user authentication and account creation through the documentation interface.

---

## 1. New Tools, Packages, and Configurations Added Today

### 1.1 Installed Documentation Tools

We installed drf-spectacular for OpenAPI schema generation and Swagger UI:

```
pip install drf-spectacular drf-spectacular-sidecar
```

These tools allowed us to:

- Automatically document all API endpoints
- Test endpoints directly in the browser
- Provide developers with a visual API overview

---

## 2. Project Configuration Updates

### 2.1 Added Spectacular Packages to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "drf_spectacular",
    "drf_spectacular_sidecar",
]
```

### 2.2 Updated REST Framework Settings

```python
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
```

### 2.3 Added Spectacular Settings

```python
SPECTACULAR_SETTINGS = {
    "TITLE": "Bank Application API",
    "DESCRIPTION": "Comprehensive API documentation for the banking backend",
    "VERSION": "1.0.0",
}
```

---

## 3. Updated URL Configuration

In `mibank/urls.py`, we added schema and Swagger paths:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
    path("transactions/", include("transactions.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
```

### Swagger Documentation URL

```
/api/docs/swagger/
```

This allowed us to **test login, register, and create account** directly inside the browser.

---

## 4. Transactions App Additions

### 4.1 Models Added Today

#### Transactions Model

```python
class Transactions(models.Model):
    sender = models.ForeignKey('accounts.Accounts', on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey('accounts.Accounts', on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.FloatField()
    status = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### LoanApplications Model

```python
class LoanApplications(models.Model):
    user = models.ForeignKey('accounts.Accounts', on_delete=models.CASCADE, related_name='user_loan')
    principal_amount = models.FloatField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

These models allow us to track:

- Sender/receiver transactions
- Loan applications tied to accounts

---

## 5. Serializers Implemented Today

```python
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplications
        fields = "__all__"
```

---

## 6. Permission System Added Today

A new permission class was created to ensure that **only current accounts** can apply for loans.

### `IscurrentAccount` Permission

```python
class IscurrentAccount(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        try:
            user_account = Accounts.objects.get(user=request.user.id)
        except Accounts.DoesNotExist:
            return False

        return request.method == "POST" and user_account.account_type == "current"
```

### Why this was needed

Loan applications follow this real-world rule:

- **Savings accounts cannot apply for loans**
- **Only current accounts are eligible**

---

## 7. Loan Application Endpoint

```python
@api_view(["POST"])
@permission_classes([IscurrentAccount])
def apply_for_loan(request):
    account = Accounts.objects.get(user=request.user.id)
    serializer = LoanSerializer(data=request.data)
    serializer.save(user=account)
    return Response({"message": "Loan application submitted successfully"})
```

---

## 8. Testing Flow Completed Today

This section replaces the deposit/transfer sections removed.

### 8.1 Creating a New User (JSON Example)

Endpoint:

```
POST /auth/register/
```

Request:

```json
{
  "first_name": "Loan",
  "last_name": "Tester",
  "email": "loan@test.com",
  "phone_number": "0701112223",
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

### 8.2 Logging in the New User (JSON Example)

Endpoint:

```
POST /auth/login/
```

Request:

```json
{
  "email": "loan@test.com",
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

We tested this login request directly inside Swagger UI to confirm that documentation was working.

---

### 8.3 Creating a New Current Account (Needed for Loan Testing)

Endpoint:

```
POST /accounts/create/
```

Request:

```json
{
  "bvn": "12345678901",
  "nin": "33445566778",
  "account_type": "current"
}
```

Response:

```json
{
  "message": "Account created successfully",
  "data": {
    "user": {
      "id": 5,
      "first_name": "Loan",
      "last_name": "Tester",
      "email": "loan@test.com",
      "phone_number": "0701112223"
    },
    "account_number": "6018622828",
    "account_type": "current",
    "amount": 0.0
  }
}
```

This step was necessary because:

- Loan permission requires current accounts
- Our original user had a savings account

---

### 8.4 Testing the Login Documentation in Swagger

We reviewed:

- Summary
- Description
- Example body
- Example response

`drf-spectacular` correctly displayed the login endpoint with:

- Schema validation
- Example JSON
- Response formats

This confirmed that documentation is functioning.

---

## 9. Transactions URLs Added Today

```python
urlpatterns = [
    path("deposit/", views.deposit),
    path("transfer/", views.transfer),
    path("loan/", views.apply_for_loan),
]
```

---

## 10. Admin Registration Completed Today

```python
admin.site.register(Transactions, TransactionAdmin)
admin.site.register(LoanApplications, LoanAdmin)
```

This allowed us to see:

- All transactions
- All loan applications

directly in the Django admin panel.

---

## 11. Errors and Challenges Faced Today

| Issue                    | Cause                                        | Solution                                      |
| ------------------------ | -------------------------------------------- | --------------------------------------------- |
| Model not found in admin | Used `Transaction` instead of `Transactions` | Corrected model names                         |
| Loan permission failing  | User had a savings account                   | Created a new **current** account             |
| Swagger not loading      | Missing schema URL                           | Added `/api/schema/` and `/api/docs/swagger/` |
| Migration issues         | New models added                             | Ran `makemigrations` and `migrate`            |

---

## 12. Concepts Learned Today

### 12.1 Custom Permissions

Used to enforce business rules such as "only current accounts can apply for loans".

### 12.2 OpenAPI / Swagger Documentation

On Day 2, we integrated **drf-spectacular** to automatically generate OpenAPI schema and display it using Swagger UI at:

```
/api/docs/swagger/
```

We applied Swagger documentation **only to the login endpoint** using `extend_schema`.
This allowed us to test the login process directly in the browser without Postman.

---

#### Example: Testing Login via Swagger

**Documented Endpoint**

```
POST /auth/login/
```

This endpoint includes:

- A summary
- A description
- A request example
- Expected response examples

All generated by the decorator:

```python
@extend_schema(
    methods=['POST'],
    request=dict,
    responses={
        200: {"message": "Login Successful"},
        400: {"message": "Login Failed"},
    },
    examples=[
        OpenApiExample(
            "Login",
            value={
                "email": "email@gmail.com",
                "password": "your pass"
            }
        )
    ],
    summary="Login User",
    description="this is for login"
)
```

---

### Swagger Login Example Used During Testing

**Request Example**

```json
{
  "email": "loan@test.com",
  "password": "StrongPass123!"
}
```

**Expected Response**

```json
{
  "message": "User Login successful",
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

Swagger allowed us to:

- Enter the login credentials
- Execute the request
- Copy the generated access token
- Use it for authenticated routes such as account creation and transactions

---

### 12.3 Admin Configuration

Improved visibility for transactions and loans.

### 12.4 Testing API Flows with Documentation

Learned how to validate endpoints using automatically generated Swagger UI.

---

## 13. Summary of Day 2

Today we successfully:

1. Installed and configured API documentation tools
2. Added Swagger and OpenAPI schema routes
3. Implemented loan features
4. Added permission classes for account-type restrictions
5. Created serializers for loans
6. Registered models in Django admin
7. Created and tested a new current account
8. Verified login and create-account endpoints in Swagger UI
9. Learned key backend documentation concepts

This completes the work for Week 11, Day 2.

---

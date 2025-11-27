
# Understanding CRUD in Django

CRUD represents the four fundamental operations used when working with data in any application:

* Create
* Read
* Update
* Delete

These operations apply to Django’s ORM, Django views, and Django REST Framework APIs.

---

# CRUD Operations in Django

Django supports CRUD through:

* Models, which define the structure of the database
* Views, which hold the logic for each operation
* URLs, which map routes to views
* Templates (for HTML-based apps) or Serializers/JSON (for APIs)

Below is a detailed breakdown of each CRUD operation.

---

## 1. Create (POST)

Creating a new record in the database.

### Django ORM Example

```python
from app.models import Customer

customer = Customer.objects.create(
    name="Cosmas",
    email="cosmas@example.com"
)
```

### Using a Django View

```python
def create_customer(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        Customer.objects.create(name=name, email=email)
        return HttpResponse("Customer created.")
```

### Using Django REST Framework

```python
class CustomerCreate(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
```

---

## 2. Read (GET)

Reading records involves either retrieving all items or a single item.

### Django ORM Example

```python
# Fetch all
customers = Customer.objects.all()

# Fetch one
customer = Customer.objects.get(id=1)
```

To avoid errors when a record does not exist:

```python
from django.shortcuts import get_object_or_404
customer = get_object_or_404(Customer, id=1)
```

### Using a Django View

```python
def get_customers(request):
    customers = Customer.objects.all()
    return render(request, "customers.html", {"customers": customers})
```

### Using Django REST Framework

```python
class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
```

---

## 3. Update (PUT / PATCH)

Updating modifies an existing record.

* PUT updates all fields
* PATCH updates only specified fields

### Django ORM Example

```python
customer = Customer.objects.get(id=1)
customer.email = "newmail@example.com"
customer.save()
```

### Using a Django View

```python
def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.name = request.POST["name"]
        customer.email = request.POST["email"]
        customer.save()
        return HttpResponse("Customer updated.")
```

### Using Django REST Framework

```python
class CustomerUpdate(APIView):
    def put(self, request, id):
        customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def patch(self, request, id):
        customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
```

---

## 4. Delete (DELETE)

Removing a record permanently from the database.

### Django ORM Example

```python
customer = Customer.objects.get(id=1)
customer.delete()
```

### Using a Django View

```python
def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return HttpResponse("Customer deleted.")
```

### Using Django REST Framework

```python
class CustomerDelete(APIView):
    def delete(self, request, id):
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
        return Response(status=204)
```

---

# CRUD Summary Table

| Operation | HTTP Method | ORM Function             | Purpose        |
| --------- | ----------- | ------------------------ | -------------- |
| Create    | POST        | `Model.objects.create()` | Add new record |
| Read      | GET         | `.get()`, `.all()`       | Retrieve data  |
| Update    | PUT/PATCH   | `.save()`                | Modify data    |
| Delete    | DELETE      | `.delete()`              | Remove record  |

---

# CRUD with Django Generic Class-Based Views

Django offers built-in class-based views that handle CRUD automatically:

| Operation     | Class      |
| ------------- | ---------- |
| Create        | CreateView |
| Read (list)   | ListView   |
| Read (detail) | DetailView |
| Update        | UpdateView |
| Delete        | DeleteView |

Example:

```python
from django.views.generic import ListView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = "customers.html"
```

---

# CRUD with Django REST Framework ViewSets

DRF provides `ModelViewSet`, which automatically generates all CRUD endpoints.

```python
from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
```

DRF automatically generates:

* POST /customers/
* GET /customers/
* GET /customers/<id>/
* PUT /customers/<id>/
* PATCH /customers/<id>/
* DELETE /customers/<id>/

---

# Final Overview

CRUD in Django involves:

1. Models to represent the database structure
2. Views to handle logic
3. Forms or serializers to validate data
4. Templates or JSON for output
5. URLs to map routes

Django and Django REST Framework provide complete support for implementing CRUD efficiently for both web apps and APIs.

---

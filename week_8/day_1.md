# What Is a Django View?

A Django view is simply a Python function (or class) that receives an HTTP request and returns an HTTP response.

The view is the “brain” of my Django project.
It decides what should happen when a user visits a URL.

---

# In simple terms:

```
URL → View → Response
```

* The URL determines which view should run.
* The view handles the logic (reading data, saving, updating, deleting, etc.).
* The view sends back a response (JSON, HTML, text, errors, etc.).

---

# Example Overview

If I have this URL:

```python
path('create_product/', views.create_product)
```

And I visit:

```
http://localhost:8000/create_product/
```

Django will run this function:

```python
def create_product(request):
    ...
```

This function will return a response to the browser or Postman.

---

# How Django Views Work Step-by-Step

## 1. I define a view

Example:

```python
from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Hello World"})
```

This is a simple view that returns JSON.

---

## 2. I connect the view to a URL

In `urls.py`:

```python
path('hello/', views.hello)
```

If I visit:

```
http://localhost:8000/hello/
```

Django will run the `hello` view.

---

## 3. Django passes the request object

Every view receives a `request`:

```python
def create_product(request):
```

This `request` contains:

* `request.method` → GET, POST, PUT, DELETE
* `request.body` → Raw request data
* `request.GET` → Query parameters
* `request.POST` → Form fields

---

# Explaining My Project Views

Here is the explanation for the views I created:

* `create_product`
* `update_product`
* `delete_product`

---

# 1. CREATE PRODUCT – Explanation

```python
def create_product(request):
    if request.method == "POST":
```

This checks if the request is a POST request.

## Extracting request body:

```python
incoming_data = request.body.decode()
to_dict = json.loads(incoming_data)
```

* `request.body` gives raw bytes
* `.decode()` converts bytes to string
* `json.loads()` converts JSON to a Python dictionary

### Adding to the list

```python
market_product.append({"id": len(market_product) + 1, **to_dict})
```

This creates a new product with an auto-incremented ID.

### Response

```python
return JsonResponse({"message": "Product created successfully"}, status=201)
```

This returns a JSON response to the user.

---

# 2. UPDATE PRODUCT – Explanation

```python
def update_product(request, id):
    if request.method == "PUT":
```

This ensures only PUT requests are allowed.

## Get incoming data

```python
incoming_data = request.body.decode()
to_dict = json.loads(incoming_data)
```

### Find the product with the matching ID

```python
for product in market_product:
    if product["id"] == id:
```

### Update the fields

```python
product["name"] = to_dict["name"]
```

I overwrite the old values with the new ones.

### Response

```python
return JsonResponse({"message": "Product updated successfully"})
```

---

# 3. DELETE PRODUCT – Explanation

```python
def delete_product(request, id):
    if request.method == "DELETE":
```

This ensures only DELETE requests are allowed.

## Find and remove the product

```python
for product in market_product:
    if product["id"] == id:
        market_product.remove(product)
```

### Response

```python
return JsonResponse({"message": "Product deleted successfully"})
```

---

# Summary: What I Should Remember About Django Views

| Concept        | Explanation                                 |
| -------------- | ------------------------------------------- |
| View           | Python function/class that handles requests |
| request        | Contains all the data sent by the user      |
| response       | What the view returns                       |
| URL mapping    | Connects a URL to a view function           |
| request.method | Helps me check GET/POST/PUT/DELETE          |
| JsonResponse   | Used to return JSON                         |

---

# Week 7 Summary

This week focused on **Django fundamentals**, building APIs, understanding HTTP response types, working with media files, URL routing, settings configuration, and creating a functional market API with sample data.

---

## **1. Starting a Django Project & App**

I learned how to:

- Create a Django project (`django-admin startproject myproject`)
- Create a Django app
- Configure project structure
- Run the development server

Django automatically generates key files such as `manage.py`, `settings.py`, `urls.py`, `views.py`, etc.

---

## **2. Django Views: Returning Different Response Types**

I practiced multiple response formats:

### **JSON Response**

```python
def say_something(request):
    return JsonResponse({"message": "Hello from the server side"})
```

### **HTML Response**

```python
def html_func(request):
    return HttpResponse("<h1>Welcome to my backend server</h1>")
```

### **XML Response**

```python
def xml_func(request):
    return HttpResponse("<message>This is a xml data</message>", content_type="application/xml")
```

### **Plain Text Response**

```python
def text_func(request):
    return HttpResponse("This is a text file")
```

### **CSV File Response (Download)**

```python
response = HttpResponse(content_type="text/csv")
response["Content-Disposition"] = 'attachment; filename="premier_league_table.csv"'
```

### **Serving Images**

- Used Pillow (PIL) to open and resize images.
- Returned processed images using `HttpResponse`.

### **Serving PDF and Video Files**

- Learned how to open binary files (`rb`) and return them.
- Handled error responses (404, 500).

---

## **3. Market App: Product API Endpoint**

We built a simple API that returns a list of products.

### **Sample Product Data**

A list of Python dictionaries representing products:

```python
market_product = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics", ...},
    {"id": 2, "name": "Laptop Backpack", ...},
    ...
]
```

### **GET Products View**

```python
def get_product(request):
    return JsonResponse({
        "message": "Get Products Successful",
        "products": market_product
    })
```

### **Market URLs**

```python
urlpatterns = [
    path('product/', views.get_product, name='get-product'),
]
```

---

## **4. Project-Level URL Routing**

I learned how Django routes URLs to views.

Key concepts:

- Using `include()` to load app-specific URLs.
- Defining routes for multiple view types.
- Serving static and media files in development.

### **Example**

```python
urlpatterns = [
    path("say/", views.say_something),
    path("text/", views.text_func),
    path("csv/", views.csv_func),
    path("xml/", views.xml_func),
    path("img/", views.image_func),
    path("pdf/", views.pdf_func),
    path("vid/", views.vid_func),
    path("market/", include("market.urls"))
]
```

---

## **5. Django Settings Configuration**

You explored important Django settings:

### **Base Settings Concepts**

- `SECRET_KEY` — keep safe in production
- `DEBUG` — development vs production
- `ALLOWED_HOSTS` — set to `['*']` for development
- `INSTALLED_APPS` — register apps
- `MIDDLEWARE` — request/response management
- `DATABASES` — SQLite3 default setup
- `STATIC_URL` and `MEDIA_URL` — serving files

### **Media Configuration**

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Used to serve:

- Images
- PDFs
- Videos

---

## **6. Running Django Tasks with manage.py**

We reviewed how Django executes commands through `manage.py`.

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
execute_from_command_line(sys.argv)
```

This is used for:

- `runserver`
- `createsuperuser`
- `migrate`
- `makemigrations`

---

# **Conclusion**

Week 7 expanded my backend skills by focusing on Django basics and content delivery through multiple formats—JSON, HTML, XML, CSV, images, PDFs, and videos. I also built my first API endpoint using Django, learned URL routing, and understood core configuration settings.

These are essential foundations for building more advanced Django applications, REST APIs, admin dashboards, and full-stack web platforms.

---

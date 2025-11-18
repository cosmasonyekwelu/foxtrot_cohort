# Django Web Development Course - Week 8: Front-End Integration & Authentication

## Course Description

This course provides a comprehensive introduction to Django, a high-level Python web framework that enables rapid development of secure and maintainable websites. Students will learn to build dynamic web applications from scratch using Django's powerful components and best practices.

## Module 1: Introduction to Front-end Development Tools

### Modern Front-end Development Ecosystem

```python
# Django project structure with front-end tools
"""
myproject/
├── frontend/                 # Front-end specific files
│   ├── src/
│   │   ├── styles/
│   │   ├── scripts/
│   │   └── components/
│   ├── package.json
│   ├── webpack.config.js
│   └── ...
├── static/                  # Django static files
│   ├── css/
│   ├── js/
│   ├── images/
│   └── ...
├── templates/               # Django templates
│   ├── base.html
│   ├── includes/
│   └── ...
└── ...
"""

# Common front-end tools and their purposes
"""
Tool              Purpose
----------------  -------------------------------------------------
npm/yarn          Package management for JavaScript
webpack           Module bundler and build tool
Babel             JavaScript compiler for modern syntax
Sass/SCSS         CSS preprocessor with advanced features
ESLint            Code linting for JavaScript
Prettier          Code formatting
Jest              JavaScript testing framework
"""

# Integration with Django
# package.json example for front-end build process
"""
{
  "name": "myproject-frontend",
  "version": "1.0.0",
  "scripts": {
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production",
    "lint": "eslint src/",
    "test": "jest"
  },
  "dependencies": {
    "axios": "^1.0.0"
  },
  "devDependencies": {
    "webpack": "^5.0.0",
    "babel-loader": "^9.0.0",
    "sass-loader": "^13.0.0",
    "css-loader": "^6.0.0"
  }
}
"""
```

## Module 2: HTML & CSS

### Django Templates with HTML & CSS

```django
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django App{% endblock %}</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">

    <!-- Block for page-specific CSS -->
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'home' %}">MyApp</a>
            <div class="navbar-nav ms-auto">
                {% if user.is_authenticated %}
                    <a class="nav-link" href="{% url 'profile' %}">Profile</a>
                    <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                {% else %}
                    <a class="nav-link" href="{% url 'login' %}">Login</a>
                    <a class="nav-link" href="{% url 'register' %}">Register</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container mt-4">
        <!-- Messages -->
        {% if messages %}
            <div class="messages">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        <!-- Page Content -->
        {% block content %}
        {% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-light mt-5 py-4">
        <div class="container text-center">
            <p>&copy; 2023 My Django App. All rights reserved.</p>
        </div>
    </footer>

    <!-- JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'js/main.js' %}"></script>

    <!-- Block for page-specific JavaScript -->
    {% block extra_js %}{% endblock %}
</body>
</html>
```

```css
/* static/css/main.css */
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --success-color: #28a745;
  --danger-color: #dc3545;
  --warning-color: #ffc107;
  --info-color: #17a2b8;
  --light-color: #f8f9fa;
  --dark-color: #343a40;
}

body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--dark-color);
  background-color: #f5f5f5;
}

/* Custom navbar */
.navbar-brand {
  font-weight: bold;
  font-size: 1.5rem;
}

/* Card styles */
.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: none;
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Form styles */
.form-control:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.btn-primary {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

/* Table styles */
.table-hover tbody tr:hover {
  background-color: rgba(0, 123, 255, 0.1);
}

/* Responsive utilities */
@media (max-width: 768px) {
  .container {
    padding-left: 15px;
    padding-right: 15px;
  }

  .navbar-nav {
    text-align: center;
  }
}

/* Custom utility classes */
.text-primary {
  color: var(--primary-color) !important;
}
.bg-primary {
  background-color: var(--primary-color) !important;
}

/* Loading spinner */
.spinner-border {
  width: 3rem;
  height: 3rem;
}
```

## Module 3: Basic JavaScript

### JavaScript in Django Templates

```django
<!-- templates/products/product_list.html -->
{% extends 'base.html' %}
{% load static %}

{% block title %}Products - My App{% endblock %}

{% block extra_css %}
<style>
    .product-card {
        transition: all 0.3s ease;
    }
    .product-card:hover {
        transform: scale(1.02);
    }
</style>
{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <h1 class="mb-4">Our Products</h1>

        <!-- Search and Filter -->
        <div class="card mb-4">
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <input type="text" id="searchInput" class="form-control" placeholder="Search products...">
                    </div>
                    <div class="col-md-6">
                        <select id="categoryFilter" class="form-select">
                            <option value="">All Categories</option>
                            {% for category in categories %}
                                <option value="{{ category.name }}">{{ category.name }}</option>
                            {% endfor %}
                        </select>
                    </div>
                </div>
            </div>
        </div>

        <!-- Products Grid -->
        <div class="row" id="productsContainer">
            {% for product in products %}
            <div class="col-lg-4 col-md-6 mb-4 product-item"
                 data-name="{{ product.name|lower }}"
                 data-category="{{ product.category.name }}">
                <div class="card product-card h-100">
                    {% if product.image %}
                    <img src="{{ product.image.url }}" class="card-img-top" alt="{{ product.name }}" style="height: 200px; object-fit: cover;">
                    {% endif %}
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text flex-grow-1">{{ product.description|truncatewords:20 }}</p>
                        <div class="mt-auto">
                            <p class="h5 text-primary">${{ product.price }}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <span class="badge bg-secondary">{{ product.category.name }}</span>
                                <button class="btn btn-primary btn-sm add-to-cart"
                                        data-product-id="{{ product.id }}"
                                        data-product-name="{{ product.name }}"
                                        data-product-price="{{ product.price }}">
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {% empty %}
            <div class="col-12">
                <div class="alert alert-info">No products found.</div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/products.js' %}"></script>
{% endblock %}
```

```javascript
// static/js/products.js
document.addEventListener("DOMContentLoaded", function () {
  // Search functionality
  const searchInput = document.getElementById("searchInput");
  const categoryFilter = document.getElementById("categoryFilter");
  const productItems = document.querySelectorAll(".product-item");

  function filterProducts() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedCategory = categoryFilter.value.toLowerCase();

    productItems.forEach((item) => {
      const productName = item.dataset.name;
      const productCategory = item.dataset.category.toLowerCase();

      const nameMatch = productName.includes(searchTerm);
      const categoryMatch =
        !selectedCategory || productCategory === selectedCategory;

      if (nameMatch && categoryMatch) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  }

  searchInput.addEventListener("input", filterProducts);
  categoryFilter.addEventListener("change", filterProducts);

  // Add to cart functionality
  const addToCartButtons = document.querySelectorAll(".add-to-cart");

  addToCartButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const productId = this.dataset.productId;
      const productName = this.dataset.productName;
      const productPrice = this.dataset.productPrice;

      addToCart(productId, productName, productPrice);
    });
  });

  function addToCart(productId, productName, productPrice) {
    // Get existing cart from localStorage or initialize empty array
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    // Check if product already in cart
    const existingItem = cart.find((item) => item.id === productId);

    if (existingItem) {
      existingItem.quantity += 1;
    } else {
      cart.push({
        id: productId,
        name: productName,
        price: parseFloat(productPrice),
        quantity: 1,
      });
    }

    // Save updated cart to localStorage
    localStorage.setItem("cart", JSON.stringify(cart));

    // Update cart count in navbar
    updateCartCount();

    // Show success message
    showAlert("Product added to cart!", "success");
  }

  function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);

    let cartBadge = document.getElementById("cartBadge");
    if (!cartBadge) {
      cartBadge = document.createElement("span");
      cartBadge.id = "cartBadge";
      cartBadge.className = "badge bg-danger ms-1";
      document
        .querySelector('.navbar-nav .nav-link[href*="cart"]')
        .appendChild(cartBadge);
    }

    cartBadge.textContent = totalItems;
  }

  function showAlert(message, type) {
    const alertDiv = document.createElement("div");
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

    document.querySelector("main .container").prepend(alertDiv);

    // Auto remove after 3 seconds
    setTimeout(() => {
      if (alertDiv.parentElement) {
        alertDiv.remove();
      }
    }, 3000);
  }

  // Initialize cart count on page load
  updateCartCount();
});
```

## Module 4: Front-End Tools as Django Templates

### Template Inheritance and Components

```django
<!-- templates/includes/header.html -->
<header class="bg-dark text-white py-3">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-md-6">
                <h1 class="h3 mb-0">
                    <a href="{% url 'home' %}" class="text-white text-decoration-none">
                        <i class="bi bi-shop"></i> MyStore
                    </a>
                </h1>
            </div>
            <div class="col-md-6 text-end">
                <div id="cart-summary">
                    {% include 'includes/cart_summary.html' %}
                </div>
            </div>
        </div>
    </div>
</header>
```

```django
<!-- templates/includes/cart_summary.html -->
{% load cart_tags %}
<div class="dropdown">
    <button class="btn btn-outline-light dropdown-toggle" type="button" data-bs-toggle="dropdown">
        <i class="bi bi-cart3"></i> Cart
        {% get_cart_count as cart_count %}
        {% if cart_count > 0 %}
        <span class="badge bg-danger">{{ cart_count }}</span>
        {% endif %}
    </button>
    <div class="dropdown-menu dropdown-menu-end">
        {% get_cart_items as cart_items %}
        {% if cart_items %}
            {% for item in cart_items %}
            <div class="dropdown-item">
                <div class="d-flex justify-content-between">
                    <span>{{ item.product.name }}</span>
                    <span>${{ item.total_price }}</span>
                </div>
                <small class="text-muted">Qty: {{ item.quantity }}</small>
            </div>
            {% endfor %}
            <div class="dropdown-divider"></div>
            <div class="dropdown-item">
                <strong>Total: ${% cart_total %}</strong>
            </div>
            <div class="dropdown-item">
                <a href="{% url 'cart_detail' %}" class="btn btn-primary btn-sm w-100">View Cart</a>
            </div>
        {% else %}
            <div class="dropdown-item text-muted">Your cart is empty</div>
        {% endif %}
    </div>
</div>
```

```django
<!-- templates/includes/pagination.html -->
{% if page_obj.has_other_pages %}
<nav aria-label="Page navigation">
    <ul class="pagination justify-content-center">
        {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page=1{% for key, value in request.GET.items %}{% if key != 'page' %}&{{ key }}={{ value }}{% endif %}{% endfor %}">First</a>
            </li>
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% for key, value in request.GET.items %}{% if key != 'page' %}&{{ key }}={{ value }}{% endif %}{% endfor %}">Previous</a>
            </li>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
                <li class="page-item active">
                    <span class="page-link">{{ num }}</span>
                </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ num }}{% for key, value in request.GET.items %}{% if key != 'page' %}&{{ key }}={{ value }}{% endif %}{% endfor %}">{{ num }}</a>
                </li>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% for key, value in request.GET.items %}{% if key != 'page' %}&{{ key }}={{ value }}{% endif %}{% endfor %}">Next</a>
            </li>
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.paginator.num_pages }}{% for key, value in request.GET.items %}{% if key != 'page' %}&{{ key }}={{ value }}{% endif %}{% endfor %}">Last</a>
            </li>
        {% endif %}
    </ul>
</nav>
{% endif %}
```

### Custom Template Tags and Filters

```python
# myapp/templatetags/cart_tags.py
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_cart_count(request):
    """Get the total number of items in cart"""
    cart = request.session.get(settings.CART_SESSION_ID, {})
    return sum(item['quantity'] for item in cart.values())

@register.simple_tag
def get_cart_items(request):
    """Get cart items with product details"""
    from myapp.models import Product
    cart = request.session.get(settings.CART_SESSION_ID, {})
    cart_items = []

    for product_id, item in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'total_price': product.price * item['quantity']
            })
        except Product.DoesNotExist:
            continue

    return cart_items

@register.simple_tag
def cart_total(request):
    """Calculate total cart value"""
    cart_items = get_cart_items(request)
    return sum(item['total_price'] for item in cart_items)

@register.filter
def multiply(value, arg):
    """Multiply value by argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def currency(value):
    """Format value as currency"""
    try:
        return f"${float(value):.2f}"
    except (ValueError, TypeError):
        return "$0.00"
```

## Module 5: Serving Static and Media Files

### Configuration and Setup

```python
# settings.py - Static and Media files configuration
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "frontend/dist",  # If using frontend build tools
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (User uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Static files finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# In production, you might want to use:
# WHITENOISE for static files
# AWS S3 for media files
```

```python
# urls.py - Serving media files in development
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

```python
# Models with file uploads
from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Product image"
    )
    document = models.FileField(
        upload_to='documents/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Product documentation"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

    def image_url(self):
        """Return image URL or default image"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/images/default-product.png'

    class Meta:
        ordering = ['-created_at']
```

## Module 6: The Django Session Framework

### Session Configuration and Usage

```python
# settings.py - Session configuration
# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default
# Alternative session backends:
# 'django.contrib.sessions.backends.cache'
# 'django.contrib.sessions.backends.cached_db'
# 'django.contrib.sessions.backends.file'
# 'django.contrib.sessions.backends.signed_cookies'

SESSION_COOKIE_NAME = 'mysessionid'
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_COOKIE_SECURE = True  # In production, use HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True  # Update session on every request
```

```python
# Using sessions in views
from django.shortcuts import render, redirect
from django.contrib import messages

def add_to_cart_session(request, product_id):
    """Add product to cart using session"""
    if request.method == 'POST':
        # Get or initialize cart in session
        cart = request.session.get('cart', {})

        # Convert product_id to string for JSON serialization
        product_id_str = str(product_id)

        # Add product to cart or increment quantity
        if product_id_str in cart:
            cart[product_id_str]['quantity'] += 1
        else:
            cart[product_id_str] = {
                'quantity': 1,
                'added_at': str(timezone.now())
            }

        # Save cart back to session
        request.session['cart'] = cart
        request.session.modified = True  # Ensure session is saved

        messages.success(request, 'Product added to cart!')

        return redirect('product_list')

    return redirect('product_list')

def view_cart_session(request):
    """Display cart contents from session"""
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    # Get product details for items in cart
    from myapp.models import Product
    for product_id, item_data in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            item_total = product.price * item_data['quantity']
            cart_items.append({
                'product': product,
                'quantity': item_data['quantity'],
                'total_price': item_total
            })
            total_price += item_total
        except Product.DoesNotExist:
            # Remove invalid products from cart
            del cart[product_id]
            request.session.modified = True

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': len(cart_items)
    }

    return render(request, 'cart/cart_detail.html', context)

def clear_cart_session(request):
    """Clear the shopping cart"""
    if 'cart' in request.session:
        del request.session['cart']
        messages.info(request, 'Cart cleared successfully.')

    return redirect('view_cart')
```

## Module 7: Sessions in Views

### Advanced Session Usage

```python
# Advanced session examples
def track_user_activity(request):
    """Track user activity using sessions"""
    # Initialize activity log if not exists
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []

    # Add current page to activity log
    current_activity = {
        'path': request.path,
        'timestamp': str(timezone.now()),
        'method': request.method
    }

    # Keep only last 10 activities
    activity_log = request.session['activity_log']
    activity_log.append(current_activity)
    if len(activity_log) > 10:
        activity_log = activity_log[-10:]

    request.session['activity_log'] = activity_log
    request.session.modified = True

    return current_activity

def user_preferences(request):
    """Manage user preferences with sessions"""
    if request.method == 'POST':
        # Save user preferences to session
        theme = request.POST.get('theme', 'light')
        language = request.POST.get('language', 'en')
        items_per_page = request.POST.get('items_per_page', 10)

        request.session['user_preferences'] = {
            'theme': theme,
            'language': language,
            'items_per_page': int(items_per_page)
        }
        request.session.modified = True

        messages.success(request, 'Preferences saved!')
        return redirect('user_profile')

    # Get current preferences or defaults
    preferences = request.session.get('user_preferences', {
        'theme': 'light',
        'language': 'en',
        'items_per_page': 10
    })

    return render(request, 'preferences.html', {'preferences': preferences})

def session_debug_view(request):
    """Debug view to show session contents"""
    session_info = {
        'session_key': request.session.session_key,
        'session_expiry': request.session.get_expiry_age(),
        'session_data': dict(request.session),
        'session_accessed': request.session.accessed,
        'session_modified': request.session.modified,
    }

    return render(request, 'debug/session_info.html', {'session_info': session_info})
```

## Module 8: Session Tuning

### Performance and Security Optimization

```python
# settings.py - Session optimization
# Session performance settings
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # Best of both worlds
SESSION_CACHE_ALIAS = 'default'  # Use default cache
SESSION_COOKIE_AGE = 3600  # 1 hour - shorter for security
SESSION_SAVE_EVERY_REQUEST = False  # Better performance

# For high-traffic sites, consider:
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
```

```python
# Custom session middleware for cleanup
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.conf import settings

class SessionCleanupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Clean up expired sessions periodically
        if hasattr(request, 'session') and request.session.session_key:
            self.cleanup_expired_sessions()

        return response

    def cleanup_expired_sessions(self):
        """Remove expired sessions from database"""
        from django.core.cache import cache

        # Run cleanup only occasionally to avoid performance hit
        import random
        if random.random() < 0.01:  # 1% chance
            Session.objects.filter(expire_date__lt=timezone.now()).delete()
            cache.clear()  # Optional: clear cache if using cached sessions
```

```python
# Session security measures
def secure_session_view(request):
    """View with session security measures"""
    # Regenerate session on login for security
    if request.method == 'POST' and 'login' in request.POST:
        # This prevents session fixation attacks
        request.session.cycle_key()

    # Check for session hijacking (basic example)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    ip_address = request.META.get('REMOTE_ADDR', '')

    session_fingerprint = f"{user_agent}_{ip_address}"

    if 'session_fingerprint' not in request.session:
        request.session['session_fingerprint'] = session_fingerprint
    else:
        if request.session['session_fingerprint'] != session_fingerprint:
            # Potential session hijacking - clear session
            request.session.flush()
            messages.warning(request, 'Security alert: Session was reset.')
            return redirect('login')

    return render(request, 'secure_page.html')
```

## Module 9: Installing Django User Authentication

### Authentication System Setup

```python
# settings.py - Authentication configuration
# Authentication settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Login/Logout URLs
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGOUT_REDIRECT_URL = '/'

# Password reset settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Development
# In production, use:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Custom user model (optional)
# AUTH_USER_MODEL = 'myapp.CustomUser'
```

```python
# urls.py - Authentication URLs
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # Built-in authentication views
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'
    ), name='logout'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'
    ), name='password_change'),

    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt'
    ), name='password_reset'),

    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Custom authentication views
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
]
```

## Module 10: Using Authentication in Views (CSRF Token)

### CSRF Protection and Authentication

```django
<!-- templates/accounts/login.html -->
{% extends 'base.html' %}

{% block title %}Login - My App{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h4 class="card-title mb-0">Login to Your Account</h4>
            </div>
            <div class="card-body">
                <form method="post" novalidate>
                    {% csrf_token %}  <!-- CSRF Token is REQUIRED -->

                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {% for error in form.non_field_errors %}
                                {{ error }}
                            {% endfor %}
                        </div>
                    {% endif %}

                    <div class="mb-3">
                        <label for="{{ form.username.id_for_label }}" class="form-label">
                            Username or Email
                        </label>
                        {{ form.username }}
                        {% if form.username.errors %}
                            <div class="invalid-feedback d-block">
                                {% for error in form.username.errors %}
                                    {{ error }}
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>

                    <div class="mb-3">
                        <label for="{{ form.password.id_for_label }}" class="form-label">
                            Password
                        </label>
                        {{ form.password }}
                        {% if form.password.errors %}
                            <div class="invalid-feedback d-block">
                                {% for error in form.password.errors %}
                                    {{ error }}
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>

                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="remember_me" name="remember_me">
                        <label class="form-check-label" for="remember_me">Remember me</label>
                    </div>

                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>

                <div class="mt-3 text-center">
                    <a href="{% url 'password_reset' %}">Forgot your password?</a>
                </div>

                <div class="mt-3 text-center">
                    <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

```python
# views.py - Authentication with CSRF
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views import View

@csrf_protect
def custom_login(request):
    """Custom login view with CSRF protection"""
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')

                # Redirect to next page or profile
                next_page = request.GET.get('next', 'profile')
                return redirect(next_page)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@method_decorator(csrf_protect, name='dispatch')
class RegisterView(View):
    """Class-based registration view with CSRF protection"""

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')

        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')

        return render(request, 'accounts/register.html', {'form': form})

# AJAX views with CSRF protection
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    """Get CSRF token for AJAX requests"""
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_protect
def ajax_login(request):
    """AJAX login endpoint"""
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful',
                    'redirect_url': reverse('profile')
                })

        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data()
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
```

## Module 11: Login and Logout

### Authentication Views and Templates

```django
<!-- templates/accounts/profile.html -->
{% extends 'base.html' %}

{% block title %}My Profile - My App{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5 class="card-title mb-0">Profile Information</h5>
            </div>
            <div class="card-body">
                <div class="text-center mb-3">
                    <div class="bg-primary rounded-circle d-inline-flex align-items-center justify-content-center"
                         style="width: 80px; height: 80px;">
                        <span class="text-white h4">{{ user.username|first|upper }}</span>
                    </div>
                </div>

                <table class="table table-borderless">
                    <tr>
                        <th>Username:</th>
                        <td>{{ user.username }}</td>
                    </tr>
                    <tr>
                        <th>Email:</th>
                        <td>{{ user.email|default:"Not provided" }}</td>
                    </tr>
                    <tr>
                        <th>Joined:</th>
                        <td>{{ user.date_joined|date:"F j, Y" }}</td>
                    </tr>
                    <tr>
                        <th>Last Login:</th>
                        <td>{{ user.last_login|date:"F j, Y g:i A"|default:"Never" }}</td>
                    </tr>
                </table>

                <div class="d-grid gap-2">
                    <a href="{% url 'password_change' %}" class="btn btn-outline-primary">
                        Change Password
                    </a>
                    <a href="{% url 'logout' %}" class="btn btn-outline-danger">
                        Logout
                    </a>
                </div>
            </div>
        </div>
    </div>

    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5 class="card-title mb-0">Recent Activity</h5>
            </div>
            <div class="card-body">
                {% if user_activity %}
                    <div class="list-group">
                        {% for activity in user_activity %}
                        <div class="list-group-item">
                            <div class="d-flex w-100 justify-content-between">
                                <h6 class="mb-1">{{ activity.action }}</h6>
                                <small>{{ activity.timestamp|timesince }} ago</small>
                            </div>
                            <p class="mb-1">{{ activity.details }}</p>
                        </div>
                        {% endfor %}
                    </div>
                {% else %}
                    <p class="text-muted">No recent activity.</p>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

```django
<!-- templates/accounts/logout.html -->
{% extends 'base.html' %}

{% block title %}Logout - My App{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h4 class="card-title mb-0">Logout</h4>
            </div>
            <div class="card-body text-center">
                <p class="lead">Are you sure you want to logout?</p>

                <form method="post">
                    {% csrf_token %}
                    <div class="d-grid gap-2 d-md-block">
                        <button type="submit" class="btn btn-danger">Yes, Logout</button>
                        <a href="{% url 'profile' %}" class="btn btn-secondary">Cancel</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

```python
# views.py - Enhanced authentication views
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def user_profile(request):
    """Enhanced user profile view"""
    # Track user activity
    track_user_login_activity(request)

    # Get user's recent activity
    user_activity = get_user_activity(request.user)

    context = {
        'user_activity': user_activity,
    }

    return render(request, 'accounts/profile.html', context)

def track_user_login_activity(request):
    """Track user login activity in session"""
    if 'login_activity' not in request.session:
        request.session['login_activity'] = []

    activity = {
        'timestamp': str(timezone.now()),
        'ip_address': get_client_ip(request),
        'user_agent': request.META.get('HTTP_USER_AGENT', '')[:100]
    }

    activities = request.session['login_activity']
    activities.append(activity)

    # Keep only last 5 activities
    if len(activities) > 5:
        activities = activities[-5:]

    request.session['login_activity'] = activities
    request.session.modified = True

def get_client_ip(request):
    """Get client IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_activity(user):
    """Get user activity from database or session"""
    # This could be expanded to track various user actions
    return [
        {
            'action': 'Profile viewed',
            'timestamp': timezone.now(),
            'details': 'You viewed your profile page'
        }
    ]
```

## Module 12: Building Your Own Login/Logout Views

### Custom Authentication Implementation

```python
# views.py - Custom authentication views
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def custom_register(request):
    """Custom registration view with additional validation"""
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        # Create form with POST data
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Additional processing before saving
            user.is_active = True  # Activate user immediately
            user.save()

            # Log the user in after registration
            login(request, user)

            # Send welcome email (you would implement this)
            # send_welcome_email(user)

            messages.success(
                request,
                f'Account created successfully! Welcome, {user.username}!'
            )

            # Redirect to next page or profile
            next_page = request.GET.get('next', 'profile')
            return redirect(next_page)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/custom_register.html', {'form': form})

class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form with additional validation"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Custom username validation
        if len(username) < 3:
            raise ValidationError('Username must be at least 3 characters long.')

        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError(
                'Username can only contain letters, numbers, and underscores.'
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')

        return email

def custom_logout(request):
    """Custom logout view with additional processing"""
    if request.method == 'POST':
        # Store logout activity before logging out
        if request.user.is_authenticated:
            track_user_logout_activity(request)

        # Perform logout
        logout(request)

        messages.info(request, 'You have been successfully logged out.')
        return redirect('home')

    # If GET request, show confirmation page
    return render(request, 'accounts/custom_logout.html')

def track_user_logout_activity(request):
    """Track user logout activity"""
    # You could log this to database or session
    print(f"User {request.user.username} logged out at {timezone.now()}")

def custom_password_change(request):
    """Custom password change view"""
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()

            # Update session after password change
            update_session_auth_hash(request, user)

            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/custom_password_change.html', {'form': form})
```

## Module 13: Authentication Decorators

### Using Decorators for Access Control

```python
# views.py - Authentication decorators
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden, JsonResponse
from functools import wraps

# Basic login requirement
@login_required
def protected_view(request):
    """View that requires login"""
    return render(request, 'protected.html')

@login_required(login_url='/custom-login/')
def custom_login_required_view(request):
    """View with custom login URL"""
    return render(request, 'custom_protected.html')

# User passes test decorator
def email_required(function=None):
    """Decorator that requires user to have an email address"""
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.email != '',
        login_url='/accounts/email-required/'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

@email_required
def email_required_view(request):
    """View that requires user to have an email"""
    return render(request, 'email_required.html')

# Staff member requirement
@staff_member_required
def staff_only_view(request):
    """View only accessible to staff members"""
    return render(request, 'staff_only.html')

# Custom permission decorators
def require_permission(permission):
    """Decorator that requires specific permission"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.has_perm(permission):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You don't have permission to access this page.")
        return _wrapped_view
    return decorator

@require_permission('myapp.can_manage_users')
def user_management_view(request):
    """View that requires specific permission"""
    return render(request, 'user_management.html')

# Multiple requirements
def superuser_required(view_func):
    """Decorator that requires superuser status"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Superuser access required.")
    return _wrapped_view

@superuser_required
@login_required
def superuser_only_view(request):
    """View only accessible to superusers"""
    return render(request, 'superuser_only.html')

# Class-based view decorators
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(login_required, name='dispatch')
class ProtectedView(View):
    """Class-based view that requires login"""

    def get(self, request):
        return render(request, 'protected_class.html')

    def post(self, request):
        # Handle POST request
        return JsonResponse({'status': 'success'})

# AJAX authentication decorator
def ajax_login_required(view_func):
    """Decorator for AJAX views that require authentication"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse(
                {'error': 'Authentication required'},
                status=401
            )
    return _wrapped_view

@ajax_login_required
def ajax_protected_view(request):
    """AJAX view that requires authentication"""
    data = {
        'message': 'This is protected data',
        'user': request.user.username
    }
    return JsonResponse(data)
```

## Module 14: Adding & Deactivating Users

### User Management Views

```python
# views.py - User management
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def is_staff_user(user):
    """Check if user is staff member"""
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def user_list(request):
    """List all users (staff only)"""
    users = User.objects.all().order_by('-date_joined')

    # Filtering
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(users, 20)  # 20 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_users': users.count(),
        'active_users': users.filter(is_active=True).count(),
    }

    return render(request, 'admin/user_list.html', context)

@login_required
@user_passes_test(is_staff_user)
def add_user(request):
    """Add new user (staff only)"""
    if request.method == 'POST':
        form = StaffUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Set additional fields
            user.is_active = form.cleaned_data.get('is_active', True)
            user.is_staff = form.cleaned_data.get('is_staff', False)

            user.save()

            messages.success(request, f'User {user.username} created successfully!')
            return redirect('user_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffUserCreationForm()

    return render(request, 'admin/add_user.html', {'form': form})

class StaffUserCreationForm(UserCreationForm):
    """User creation form for staff members"""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                 'is_active', 'is_staff', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email required
        self.fields['email'].required = True

@login_required
@user_passes_test(is_staff_user)
def deactivate_user(request, user_id):
    """Deactivate user (staff only)"""
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        if user == request.user:
            messages.error(request, 'You cannot deactivate your own account!')
        else:
            user.is_active = False
            user.save()

            messages.success(request, f'User {user.username} has been deactivated.')

        return redirect('user_list')

    context = {'user': user}
    return render(request, 'admin/confirm_deactivate.html', context)

@login_required
@user_passes_test(is_staff_user)
def activate_user(request, user_id):
    """Activate user (staff only)"""
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.is_active = True
        user.save()

        messages.success(request, f'User {user.username} has been activated.')
        return redirect('user_list')

    context = {'user': user}
    return render(request, 'admin/confirm_activate.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    """Delete user (superusers only)"""
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        if user == request.user:
            messages.error(request, 'You cannot delete your own account!')
        else:
            username = user.username
            user.delete()

            messages.success(request, f'User {username} has been deleted.')

        return redirect('user_list')

    context = {'user': user}
    return render(request, 'admin/confirm_delete.html', context)

@login_required
def edit_profile(request):
    """Allow users to edit their own profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})

class UserProfileForm(forms.ModelForm):
    """Form for users to edit their profile"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if email is already used by another user
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email address is already in use.')

        return email
```

This comprehensive Week 8 module covers front-end integration, session management, and authentication in Django, providing students with the knowledge needed to build secure, interactive web applications with proper user management and front-end functionality.

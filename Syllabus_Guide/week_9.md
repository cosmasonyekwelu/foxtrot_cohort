# Django Web Development Course - Week 9: Templates & Forms

## Course Description
This course provides a comprehensive introduction to Django, a high-level Python web framework that enables rapid development of secure and maintainable websites. Students will learn to build dynamic web applications from scratch using Django's powerful components and best practices.

## Module 1: Template Fundamentals

### Understanding Django Templates

```python
# Django templates are text files that contain:
# - Static content (HTML, CSS, JavaScript)
# - Dynamic content using template variables {{ variable }}
# - Logic using template tags {% tag %}
# - Filters for modifying variables {{ variable|filter }}

# Basic template example
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>Welcome, {{ user.username }}!</h1>
    
    {% if user.is_authenticated %}
        <p>You are logged in.</p>
    {% else %}
        <p>Please log in.</p>
    {% endif %}
    
    <ul>
    {% for item in items %}
        <li>{{ item.name|title }} - ${{ item.price }}</li>
    {% empty %}
        <li>No items available.</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

# Template configuration in settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Project-level templates
        ],
        'APP_DIRS': True,  # Look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [  # Custom template tag libraries
                'myapp.templatetags.custom_filters',
            ],
        },
    },
]
```

## Module 2: Creating Template Objects

### Working with Templates Programmatically

```python
# Creating and using templates programmatically
from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse

def basic_template_view(request):
    # Method 1: Create Template from string
    template_string = """
    <h1>Hello, {{ name }}!</h1>
    <p>Welcome to {{ site_name }}.</p>
    {% if items %}
        <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    """
    
    template = Template(template_string)
    context = Context({
        'name': 'John Doe',
        'site_name': 'My Django Site',
        'items': ['Apple', 'Banana', 'Orange']
    })
    
    rendered_content = template.render(context)
    return HttpResponse(rendered_content)

def template_from_file_view(request):
    # Method 2: Load template from file
    template = get_template('myapp/greeting.html')
    
    context = {
        'user': request.user,
        'current_time': timezone.now(),
        'products': [
            {'name': 'Laptop', 'price': 999.99},
            {'name': 'Mouse', 'price': 29.99},
            {'name': 'Keyboard', 'price': 79.99},
        ]
    }
    
    rendered_content = template.render(context)
    return HttpResponse(rendered_content)

# Advanced template usage
def advanced_template_usage(request):
    # Using multiple templates
    base_template = Template("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}Default Title{% endblock %}</title>
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
    </html>
    """)
    
    content_template = Template("""
    {% extends "base.html" %}
    
    {% block title %}{{ page_title }}{% endblock %}
    
    {% block content %}
        <h1>{{ heading }}</h1>
        {{ content }}
    {% endblock %}
    """)
    
    # Create context with different data
    context = Context({
        'page_title': 'Custom Page',
        'heading': 'Welcome to Our Site',
        'content': 'This is the main content area.'
    })
    
    return HttpResponse(content_template.render(context))
```

## Module 3: Loading Template Files

### Template Loading Mechanisms

```python
# Template loader examples and configurations
from django.template.loader import get_template, render_to_string, select_template

def template_loading_examples(request):
    # Method 1: get_template - loads a single template
    template = get_template('products/list.html')
    
    # Method 2: render_to_string - template + context = rendered string
    html_content = render_to_string('email/welcome.html', {
        'user': request.user,
        'activation_url': 'http://example.com/activate/123/'
    })
    
    # Method 3: select_template - tries multiple templates, uses first found
    template = select_template([
        'products/special_list.html',  # Custom template for specific case
        'products/list.html',          # Fallback template
        'products/default_list.html'   # Ultimate fallback
    ])
    
    # Method 4: Loading templates from different apps
    admin_template = get_template('admin/base_site.html')
    auth_template = get_template('registration/login.html')
    
    return HttpResponse("Template loading examples")

# Custom template loader example
from django.template.loaders.base import Loader
from django.template import TemplateDoesNotExist
import requests

class DatabaseTemplateLoader(Loader):
    """Custom template loader that loads templates from database"""
    
    def load_template_source(self, template_name, template_dirs=None):
        # Check if template exists in database
        from myapp.models import Template
        try:
            template_obj = Template.objects.get(name=template_name)
            return template_obj.content, template_name
        except Template.DoesNotExist:
            raise TemplateDoesNotExist(template_name)

# Register custom loader in settings.py
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'LOADERS': [
            'myapp.loaders.DatabaseTemplateLoader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
    },
]
"""

# Template directory structure best practices
"""
templates/
├── base.html                 # Base template
├── includes/                 # Reusable template parts
│   ├── header.html
│   ├── footer.html
│   ├── navigation.html
│   └── messages.html
├── myapp/                    # App-specific templates
│   ├── product_list.html
│   ├── product_detail.html
│   └── product_form.html
├── registration/             # Auth templates (override)
│   ├── login.html
│   └── password_reset.html
└── admin/                    # Admin templates (override)
    └── base_site.html
"""
```

## Module 4: Filling in Template Content (Context Objects)

### Context Objects and Variable Resolution

```python
# Working with context objects
from django.template import Context
from django.shortcuts import render

def context_examples(request):
    # Basic context
    context = {
        'title': 'My Page',
        'user': request.user,
        'products': Product.objects.all()[:10],
        'current_time': timezone.now(),
    }
    
    # Using Context class for advanced features
    context_obj = Context({
        'name': 'John Doe',
        'age': 30,
    })
    
    # Adding variables to context
    context_obj['email'] = 'john@example.com'
    context_obj.update({
        'city': 'New York',
        'country': 'USA'
    })
    
    # Context with auto-escaping
    context_obj.autoescape = True
    
    return render(request, 'example.html', context)

def advanced_context_usage(request):
    # Nested context data
    context = {
        'page': {
            'title': 'Product Details',
            'description': 'Detailed product information',
            'keywords': ['electronics', 'gadgets', 'tech'],
        },
        'user_profile': {
            'personal': {
                'name': 'Jane Smith',
                'email': 'jane@example.com',
            },
            'preferences': {
                'theme': 'dark',
                'language': 'en',
            }
        },
        'products': [
            {
                'name': 'Smartphone',
                'price': 699.99,
                'specs': {
                    'storage': '128GB',
                    'ram': '8GB',
                    'camera': '48MP'
                }
            },
            {
                'name': 'Laptop',
                'price': 1299.99,
                'specs': {
                    'storage': '512GB',
                    'ram': '16GB',
                    'display': '15.6"'
                }
            }
        ]
    }
    
    return render(request, 'advanced_example.html', context)

# Custom context processors
def custom_context_processor(request):
    """Add custom variables to all templates"""
    return {
        'SITE_NAME': 'My Django Site',
        'SITE_VERSION': '1.0.0',
        'CURRENT_YEAR': timezone.now().year,
        'GOOGLE_ANALYTICS_ID': 'UA-XXXXX-Y',
    }

def shopping_cart_context(request):
    """Add shopping cart information to context"""
    cart_count = 0
    cart_total = 0
    
    if hasattr(request, 'session'):
        cart = request.session.get('cart', {})
        cart_count = sum(item.get('quantity', 0) for item in cart.values())
        # Calculate total would require product prices from database
    
    return {
        'cart_count': cart_count,
        'cart_total': cart_total,
    }

# Register context processors in settings.py
"""
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # Default processors
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom processors
                'myapp.context_processors.custom_context_processor',
                'myapp.context_processors.shopping_cart_context',
            ],
        },
    },
]
"""
```

## Module 5: Template Tags

### Built-in and Custom Template Tags

```django
<!-- Using built-in template tags -->
{% load static %}
{% load i18n %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Default Title{% endblock %}</title>
    
    <!-- Static files -->
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    <script src="{% static 'js/app.js' %}"></script>
</head>
<body>
    <!-- URL tags -->
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'products:list' %}">Products</a>
        <a href="{% url 'about' %}">About</a>
        
        {% if user.is_authenticated %}
            <a href="{% url 'profile' user.id %}">Profile</a>
            <a href="{% url 'logout' %}">Logout</a>
        {% else %}
            <a href="{% url 'login' %}">Login</a>
            <a href="{% url 'register' %}">Register</a>
        {% endif %}
    </nav>

    <!-- Block and extends tags -->
    <main>
        {% block content %}
        {% endblock %}
    </main>

    <!-- Include tags -->
    <footer>
        {% include 'includes/footer.html' %}
    </footer>

    <!-- CSRF token for forms -->
    <form method="post">
        {% csrf_token %}
        <!-- form fields -->
    </form>
</body>
</html>
```

```python
# Creating custom template tags
# myapp/templatetags/custom_tags.py
from django import template
from django.utils import timezone
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def current_time(format_string):
    """Display current time in specified format"""
    return timezone.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def user_greeting(context):
    """Personalized greeting for user"""
    request = context['request']
    if request.user.is_authenticated:
        return f"Hello, {request.user.username}!"
    return "Hello, Guest!"

@register.simple_tag
def render_stars(rating, max_rating=5):
    """Render star rating"""
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    empty_stars = max_rating - full_stars - (1 if half_star else 0)
    
    stars = '★' * full_stars
    if half_star:
        stars += '½'
    stars += '☆' * empty_stars
    
    return stars

@register.inclusion_tag('includes/product_card.html')
def product_card(product):
    """Render product card component"""
    return {'product': product}

@register.inclusion_tag('includes/pagination.html', takes_context=True)
def pagination(context, page_obj):
    """Render pagination component"""
    request = context['request']
    return {
        'page_obj': page_obj,
        'request': request,
    }

# Advanced template tags
@register.simple_tag
def calculate_discount(original_price, discount_percent):
    """Calculate discounted price"""
    discount_amount = original_price * (discount_percent / 100)
    return original_price - discount_amount

@register.simple_tag
def get_related_products(product, count=4):
    """Get related products"""
    return product.category.products.exclude(id=product.id)[:count]

# Using custom tags in templates
"""
{% load custom_tags %}

<!-- Simple tag -->
<p>Current time: {% current_time "%Y-%m-%d %H:%M" %}</p>

<!-- Tag with context -->
<div class="greeting">{% user_greeting %}</div>

<!-- Star rating -->
<div>Rating: {% render_stars product.rating %}</div>

<!-- Inclusion tag -->
{% product_card product %}

<!-- Pagination -->
{% pagination page_obj %}
"""
```

## Module 6: Template Filters

### Built-in and Custom Filters

```django
<!-- Using built-in template filters -->
<p>{{ user.username|title }} - {{ user.date_joined|date:"F j, Y" }}</p>

<p>{{ product.description|truncatewords:30 }}</p>

<p>Price: ${{ product.price|floatformat:2 }}</p>

<p>Items: {{ items|length }}</p>

<p>{{ html_content|safe }}</p>

<p>{{ text|linebreaks }}</p>

<p>{{ value|default:"Not provided" }}</p>

<p>{{ list|join:", " }}</p>

<p>{{ string|lower }}</p>

<p>{{ string|upper }}</p>

<p>{{ name|slice:":10" }}</p>

<!-- Chaining filters -->
<p>{{ product.name|title|truncatechars:20 }}</p>

<p>{{ description|striptags|truncatewords:50 }}</p>
```

```python
# Creating custom template filters
# myapp/templatetags/custom_filters.py
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply value by argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def divide(value, arg):
    """Divide value by argument"""
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0

@register.filter
@stringfilter
def truncate_chars(value, max_length):
    """Truncate string to specified number of characters"""
    if len(value) <= max_length:
        return value
    return value[:max_length] + '...'

@register.filter
def percentage(value, decimal_places=1):
    """Format value as percentage"""
    try:
        return f"{float(value) * 100:.{decimal_places}f}%"
    except (ValueError, TypeError):
        return "0%"

@register.filter
def format_currency(value, currency_symbol='$'):
    """Format value as currency"""
    try:
        return f"{currency_symbol}{float(value):,.2f}"
    except (ValueError, TypeError):
        return f"{currency_symbol}0.00"

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary using key"""
    return dictionary.get(key)

@register.filter
def in_list(value, the_list):
    """Check if value is in list"""
    return value in the_list

@register.filter(is_safe=True)
def highlight_search(text, search_term):
    """Highlight search term in text"""
    if not search_term:
        return text
    
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    highlighted = pattern.sub(
        lambda match: f'<mark>{match.group()}</mark>', 
        str(text)
    )
    return mark_safe(highlighted)

@register.filter
def human_readable_size(value):
    """Convert file size to human readable format"""
    try:
        value = int(value)
    except (TypeError, ValueError):
        return "0 B"
    
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if value < 1024.0:
            return f"{value:.1f} {unit}"
        value /= 1024.0
    return f"{value:.1f} PB"

# Advanced filters with auto-escaping
@register.filter(needs_autoescape=True)
def phone_format(value, autoescape=True):
    """Format phone number"""
    if autoescape:
        value = conditional_escape(value)
    
    if not value:
        return ""
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', str(value))
    
    if len(digits) == 10:
        return mark_safe(f"({digits[:3]}) {digits[3:6]}-{digits[6:]}")
    elif len(digits) == 11 and digits[0] == '1':
        return mark_safe(f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}")
    
    return value

# Using custom filters in templates
"""
{% load custom_filters %}

<p>Total: ${{ price|multiply:quantity }}</p>

<p>Discount: {{ discount_rate|percentage }}</p>

<p>Price: {{ product.price|format_currency }}</p>

<p>File size: {{ file.size|human_readable_size }}</p>

<p>Phone: {{ user.phone|phone_format }}</p>

<p>{{ text|highlight_search:query }}</p>

<p>{{ user_data|get_item:"email" }}</p>

{% if product.id|in_list:favorite_products %}
    <span class="favorite">★</span>
{% endif %}
"""
```

## Module 7: More on For Loops

### Advanced Loop Techniques

```django
<!-- Advanced for loop examples -->
<table class="table table-striped">
    <thead>
        <tr>
            <th>#</th>
            <th>Product</th>
            <th>Price</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        {% for product in products %}
            <tr class="{% cycle 'row-even' 'row-odd' %} 
                       {% if forloop.first %}first-row{% endif %}
                       {% if forloop.last %}last-row{% endif %}">
                
                <!-- Loop counter -->
                <td>{{ forloop.counter }}</td>
                
                <!-- Reverse counter -->
                <td>{{ forloop.revcounter }}</td>
                
                <!-- Product information -->
                <td>
                    <strong>{{ product.name }}</strong>
                    {% if product.featured %}
                        <span class="badge bg-warning">Featured</span>
                    {% endif %}
                </td>
                
                <td>${{ product.price }}</td>
                
                <td>
                    {% if product.stock_quantity > 10 %}
                        <span class="text-success">In Stock</span>
                    {% elif product.stock_quantity > 0 %}
                        <span class="text-warning">Low Stock</span>
                    {% else %}
                        <span class="text-danger">Out of Stock</span>
                    {% endif %}
                </td>
            </tr>
            
            <!-- Empty clause -->
            {% empty %}
            <tr>
                <td colspan="4" class="text-center text-muted">
                    No products found.
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>

<!-- Nested loops -->
<div class="categories">
    {% for category in categories %}
        <div class="category">
            <h3>{{ category.name }}</h3>
            <div class="products">
                {% for product in category.products.all %}
                    <div class="product">
                        <h4>{{ product.name }}</h4>
                        <p>${{ product.price }}</p>
                    </div>
                    
                    <!-- Break after 3 products per category -->
                    {% if forloop.counter >= 3 %}
                        <p>... and {{ category.products.count|add:"-3" }} more</p>
                        {% break %}
                    {% endif %}
                {% endfor %}
            </div>
        </div>
    {% endfor %}
</div>

<!-- Loop with filters -->
<ul>
    {% for user in users|dictsort:"last_name" %}
        <li>{{ user.first_name }} {{ user.last_name }}</li>
    {% endfor %}
</ul>

<!-- Regrouping data -->
{% regroup cities by country as country_list %}

{% for country in country_list %}
    <h3>{{ country.grouper }}</h3>
    <ul>
        {% for city in country.list %}
            <li>{{ city.name }} - Population: {{ city.population }}</li>
        {% endfor %}
    </ul>
{% endfor %}

<!-- Loop with range -->
{% for i in "x"|ljust:10 %}
    <span class="star">⭐</span>
{% endfor %}

<!-- Advanced cycle usage -->
<div class="row">
    {% for product in products %}
        <div class="col-md-{{ forloop.counter0|divisibleby:2|yesno:'6,4' }}">
            {% include 'includes/product_card.html' with product=product %}
        </div>
        
        <!-- Row break every 2 items -->
        {% if forloop.counter|divisibleby:2 and not forloop.last %}
            </div><div class="row mt-3">
        {% endif %}
    {% endfor %}
</div>
```

## Module 8: Template Inheritance

### Master Templates and Block System

```django
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    {% block meta %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{% block meta_description %}Default description{% endblock %}">
    <meta name="keywords" content="{% block meta_keywords %}django, python, web{% endblock %}">
    {% endblock %}
    
    <title>{% block title %}My Django Site{% endblock %}</title>
    
    {% block styles %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    {% endblock %}
    
    {% block extra_styles %}{% endblock %}
</head>
<body>
    {% block body %}
    <div id="wrapper">
        {% block header %}
        <header class="bg-dark text-white">
            <div class="container">
                <nav class="navbar navbar-expand-lg navbar-dark">
                    <a class="navbar-brand" href="{% url 'home' %}">MySite</a>
                    
                    {% block navigation %}
                    <div class="navbar-nav ms-auto">
                        <a class="nav-link" href="{% url 'home' %}">Home</a>
                        <a class="nav-link" href="{% url 'products:list' %}">Products</a>
                        <a class="nav-link" href="{% url 'about' %}">About</a>
                        
                        {% if user.is_authenticated %}
                            <a class="nav-link" href="{% url 'profile' %}">Profile</a>
                            <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                        {% else %}
                            <a class="nav-link" href="{% url 'login' %}">Login</a>
                            <a class="nav-link" href="{% url 'register' %}">Register</a>
                        {% endif %}
                    </div>
                    {% endblock %}
                </nav>
            </div>
        </header>
        {% endblock %}

        {% block messages %}
        {% if messages %}
            <div class="container mt-3">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            </div>
        {% endif %}
        {% endblock %}

        <main>
            {% block content %}
            <!-- Main content goes here -->
            {% endblock %}
        </main>

        {% block footer %}
        <footer class="bg-light mt-5 py-4">
            <div class="container text-center">
                <p>&copy; {% now "Y" %} My Django Site. All rights reserved.</p>
            </div>
        </footer>
        {% endblock %}
    </div>
    {% endblock %}

    {% block scripts %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'js/main.js' %}"></script>
    {% endblock %}

    {% block extra_scripts %}{% endblock %}
</body>
</html>
```

```django
<!-- templates/products/product_list.html -->
{% extends 'base.html' %}
{% load static %}

{% block meta_description %}Browse our amazing collection of products. Find the best deals and latest items.{% endblock %}
{% block meta_keywords %}products, shopping, ecommerce, buy online{% endblock %}

{% block title %}Products - My Site{% endblock %}

{% block extra_styles %}
<style>
    .product-card {
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: translateY(-5px);
    }
</style>
{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="row">
        <div class="col-12">
            <h1 class="mb-4">Our Products</h1>
            
            <!-- Breadcrumb -->
            {% block breadcrumb %}
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
                    <li class="breadcrumb-item active">Products</li>
                </ol>
            </nav>
            {% endblock %}

            <!-- Product filters -->
            {% include 'products/includes/filters.html' %}

            <!-- Products grid -->
            <div class="row">
                {% for product in products %}
                    <div class="col-lg-4 col-md-6 mb-4">
                        {% include 'products/includes/product_card.html' with product=product %}
                    </div>
                {% empty %}
                    <div class="col-12">
                        <div class="alert alert-info">
                            No products found. Please try different filters.
                        </div>
                    </div>
                {% endfor %}
            </div>

            <!-- Pagination -->
            {% if is_paginated %}
                {% include 'includes/pagination.html' with page_obj=page_obj %}
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}

{% block extra_scripts %}
<script src="{% static 'js/products.js' %}"></script>
{% endblock %}
```

```django
<!-- templates/products/product_detail.html -->
{% extends 'base.html' %}
{% load static custom_filters %}

{% block title %}{{ product.name }} - My Site{% endblock %}

{% block meta_description %}{{ product.description|truncatewords:20 }}{% endblock %}

{% block breadcrumb %}
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
        <li class="breadcrumb-item"><a href="{% url 'products:list' %}">Products</a></li>
        <li class="breadcrumb-item active">{{ product.name|truncatewords:3 }}</li>
    </ol>
</nav>
{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="row">
        <div class="col-md-6">
            {% if product.image %}
                <img src="{{ product.image.url }}" alt="{{ product.name }}" class="img-fluid rounded">
            {% else %}
                <img src="{% static 'images/default-product.png' %}" alt="No image" class="img-fluid rounded">
            {% endif %}
        </div>
        
        <div class="col-md-6">
            <h1>{{ product.name }}</h1>
            <p class="h3 text-primary">{{ product.price|format_currency }}</p>
            
            <div class="mb-3">
                <span class="badge bg-secondary">{{ product.category.name }}</span>
                {% if product.featured %}
                    <span class="badge bg-warning">Featured</span>
                {% endif %}
            </div>
            
            <p class="lead">{{ product.description }}</p>
            
            {% if product.in_stock %}
                <div class="d-grid gap-2 d-md-flex">
                    <button class="btn btn-primary btn-lg">Add to Cart</button>
                    <button class="btn btn-outline-secondary btn-lg">Add to Wishlist</button>
                </div>
            {% else %}
                <div class="alert alert-warning">
                    This product is currently out of stock.
                </div>
            {% endif %}
            
            <!-- Product specifications -->
            {% if product.specifications %}
                <div class="mt-4">
                    <h5>Specifications</h5>
                    <table class="table table-sm">
                        {% for key, value in product.specifications.items %}
                            <tr>
                                <th>{{ key|title }}</th>
                                <td>{{ value }}</td>
                            </tr>
                        {% endfor %}
                    </table>
                </div>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
```

## Module 9: Easy Rendering of Templates

### Shortcut Functions and Best Practices

```python
# Easy template rendering with shortcuts
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse

def simple_render_view(request):
    """Basic template rendering"""
    context = {
        'title': 'Welcome Page',
        'users': User.objects.all()[:5],
        'current_time': timezone.now(),
    }
    return render(request, 'welcome.html', context)

def render_with_different_context(request):
    """Render template with different context types"""
    # Simple context
    simple_context = {'message': 'Hello World'}
    
    # Complex nested context
    complex_context = {
        'page': {
            'title': 'Product Catalog',
            'meta': {
                'description': 'Browse our products',
                'keywords': ['electronics', 'gadgets']
            }
        },
        'products': [
            {
                'name': 'Laptop',
                'price': 999.99,
                'features': ['Fast', 'Lightweight', 'Durable']
            },
            {
                'name': 'Phone',
                'price': 699.99,
                'features': ['5G', 'Great Camera', 'Long Battery']
            }
        ]
    }
    
    return render(request, 'catalog.html', complex_context)

def render_to_string_example(request):
    """Render template to string for email or API responses"""
    # Render template to string for email
    email_content = render_to_string('email/welcome.html', {
        'user': request.user,
        'activation_link': 'http://example.com/activate/123/'
    })
    
    # Render template to string for PDF generation
    pdf_html = render_to_string('reports/invoice.html', {
        'invoice': invoice,
        'company': company_info,
    })
    
    return HttpResponse("Template rendered to string")

def conditional_rendering(request, template_name):
    """Conditional template rendering"""
    templates = {
        'mobile': 'mobile/home.html',
        'tablet': 'tablet/home.html',
        'desktop': 'desktop/home.html',
    }
    
    # Detect device type (simplified)
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if 'mobile' in user_agent:
        template = templates['mobile']
    elif 'tablet' in user_agent:
        template = templates['tablet']
    else:
        template = templates['desktop']
    
    return render(request, template, {'user_agent': user_agent})

def json_response_with_template(request):
    """Return JSON response with rendered HTML"""
    products = Product.objects.filter(available=True)
    
    # Render product list HTML
    products_html = render_to_string('products/includes/product_list.html', {
        'products': products
    })
    
    return JsonResponse({
        'success': True,
        'html': products_html,
        'count': products.count()
    })

# Template rendering best practices
def optimized_rendering(request):
    """Optimized template rendering with selective loading"""
    # Use select_related and prefetch_related to reduce database queries
    products = Product.objects.select_related('category').prefetch_related('tags')[:20]
    
    # Use values() or values_list() when you only need specific fields
    product_titles = Product.objects.values_list('name', flat=True)[:10]
    
    # Use aggregation to reduce data processing in templates
    from django.db.models import Count, Avg
    category_stats = Category.objects.annotate(
        product_count=Count('products'),
        avg_price=Avg('products__price')
    )
    
    context = {
        'products': products,
        'product_titles': product_titles,
        'category_stats': category_stats,
    }
    
    return render(request, 'optimized.html', context)
```

## Module 10: Django Form Classes

### Form Fundamentals and Creation

```python
# Basic form creation
from django import forms
from django.core.validators import validate_email, MinLengthValidator

class ContactForm(forms.Form):
    # Basic field types
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        validators=[validate_email],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    
    subject = forms.ChoiceField(
        choices=[
            ('general', 'General Inquiry'),
            ('support', 'Technical Support'),
            ('billing', 'Billing Issue'),
            ('other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Enter your message...'
        }),
        validators=[MinLengthValidator(10)]
    )
    
    newsletter = forms.BooleanField(
        required=False,
        initial=True,
        label='Subscribe to newsletter'
    )
    
    priority = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        widget=forms.RadioSelect,
        initial='medium'
    )
    
    attachment = forms.FileField(
        required=False,
        label='Attach file (optional)'
    )

# Form usage in views
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Process cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email, save to database, etc.
            send_contact_email(name, email, message)
            
            messages.success(request, 'Your message has been sent!')
            return redirect('contact_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
```

```django
<!-- templates/contact.html -->
{% extends 'base.html' %}

{% block title %}Contact Us{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h2 class="card-title">Contact Us</h2>
            </div>
            <div class="card-body">
                <form method="post" enctype="multipart/form-data" novalidate>
                    {% csrf_token %}
                    
                    <!-- Display non-field errors -->
                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {% for error in form.non_field_errors %}
                                {{ error }}
                            {% endfor %}
                        </div>
                    {% endif %}
                    
                    <!-- Manual field rendering with error handling -->
                    <div class="mb-3">
                        <label for="{{ form.name.id_for_label }}" class="form-label">
                            {{ form.name.label }}
                        </label>
                        {{ form.name }}
                        {% if form.name.errors %}
                            <div class="invalid-feedback d-block">
                                {% for error in form.name.errors %}
                                    {{ error }}
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <!-- Automated field rendering -->
                    {% for field in form %}
                        {% if field.name != 'name' %}  <!-- We already rendered name manually -->
                        <div class="mb-3">
                            <label for="{{ field.id_for_label }}" class="form-label">
                                {{ field.label }}
                            </label>
                            {{ field }}
                            
                            {% if field.help_text %}
                                <div class="form-text">{{ field.help_text }}</div>
                            {% endif %}
                            
                            {% if field.errors %}
                                <div class="invalid-feedback d-block">
                                    {% for error in field.errors %}
                                        {{ error }}
                                    {% endfor %}
                                </div>
                            {% endif %}
                        </div>
                        {% endif %}
                    {% endfor %}
                    
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## Module 11: Creating Forms from Models

### ModelForm Usage

```python
# ModelForm creation
from django import forms
from django.contrib.auth.models import User
from .models import Product, Category, Order, Customer

class ProductForm(forms.ModelForm):
    # Add extra fields not in the model
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., electronics, gadget, tech'
        })
    )
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Product Name',
            'available': 'In Stock',
        }
        help_texts = {
            'description': 'Provide detailed product description',
        }
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError("Product name must be at least 3 characters long.")
        return name

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        
        return user

# Form usage in views
@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            
            # Process tags
            tags = form.cleaned_data.get('tags', '')
            if tags:
                product.tags.set([tag.strip() for tag in tags.split(',')])
            
            messages.success(request, 'Product created successfully!')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
        # Pre-populate tags field
        if product.tags.exists():
            form.fields['tags'].initial = ', '.join(tag.name for tag in product.tags.all())
    
    return render(request, 'products/product_form.html', {'form': form})
```

## Module 12: Validation

### Form and Model Validation

```python
# Comprehensive validation examples
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re

class AdvancedProductForm(forms.ModelForm):
    # Custom validators
    sku_validator = RegexValidator(
        regex=r'^[A-Z]{3}-[0-9]{6}$',
        message='SKU must be in format: ABC-123456'
    )
    
    sku = forms.CharField(
        max_length=10,
        validators=[sku_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    discount_percentage = forms.IntegerField(
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0',
            'max': '100'
        })
    )
    
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'discount_percentage', 'category']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        # Check for profanity (simplified example)
        profanity_words = ['badword1', 'badword2']
        for word in profanity_words:
            if word in name.lower():
                raise ValidationError("Product name contains inappropriate language.")
        
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        discount_percentage = cleaned_data.get('discount_percentage')
        
        # Cross-field validation
        if price and discount_percentage:
            discounted_price = price * (1 - discount_percentage / 100)
            if discounted_price < 0:
                raise ValidationError(
                    "Discount percentage is too high. Resulting price would be negative."
                )
        
        return cleaned_data

# Model-level validation
class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def clean(self):
        # Model validation (called by full_clean())
        if self.price < self.cost_price:
            raise ValidationError({
                'price': 'Selling price cannot be lower than cost price.'
            })
        
        if self.price <= 0:
            raise ValidationError({
                'price': 'Price must be greater than zero.'
            })
    
    def save(self, *args, **kwargs):
        # Run validation before saving
        self.full_clean()
        super().save(*args, **kwargs)

# Custom validation functions
def validate_email_domain(value):
    """Validate that email is from allowed domains"""
    allowed_domains = ['example.com', 'mycompany.com']
    domain = value.split('@')[-1]
    
    if domain not in allowed_domains:
        raise ValidationError(
            f'Email domain {domain} is not allowed. '
            f'Allowed domains: {", ".join(allowed_domains)}'
        )

def validate_phone_number(value):
    """Validate phone number format"""
    pattern = r'^\+?1?\d{9,15}$'
    if not re.match(pattern, value):
        raise ValidationError('Enter a valid phone number.')

class CustomerForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_email_domain])
    phone = forms.CharField(validators=[validate_phone_number])
    
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']
```

## Module 13: Authentication

### Custom Authentication Forms

```python
# Custom authentication forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Allow login with email or username
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                username = user.username
            except User.DoesNotExist:
                raise ValidationError(
                    "No account found with this email address."
                )
        
        return username

class EnhancedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        
        return user

# Password change form with strength validation
class CustomPasswordChangeForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            MinLengthValidator(8),
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]',
                message='Password must contain uppercase, lowercase, digit and special character.'
            )
        ]
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
    
    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_password):
            raise ValidationError("Current password is incorrect.")
        return current_password
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError("New passwords don't match.")
        
        return cleaned_data
```

## Module 14: Advanced Forms Processing Techniques

### Advanced Form Handling

```python
# Advanced form processing techniques
from django.forms import formset_factory, modelformset_factory, inlineformset_factory

# Formset examples
ProductFormSet = formset_factory(ProductForm, extra=2, max_num=5)

def bulk_product_create(request):
    if request.method == 'POST':
        formset = ProductFormSet(request.POST, request.FILES)
        
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:  # Skip empty forms
                    product = form.save(commit=False)
                    product.created_by = request.user
                    product.save()
            
            messages.success(request, 'Products created successfully!')
            return redirect('product_list')
    else:
        formset = ProductFormSet()
    
    return render(request, 'products/bulk_create.html', {'formset': formset})

# Model formset
ProductModelFormSet = modelformset_factory(
    Product, 
    fields=['name', 'price', 'available'],
    extra=1,
    can_delete=True
)

def manage_products(request):
    if request.method == 'POST':
        formset = ProductModelFormSet(request.POST, queryset=Product.objects.all())
        
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Products updated successfully!')
            return redirect('manage_products')
    else:
        formset = ProductModelFormSet(queryset=Product.objects.all())
    
    return render(request, 'products/manage.html', {'formset': formset})

# Inline formset for related objects
OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    fields=['product', 'quantity', 'price'],
    extra=1,
    can_delete=True
)

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        
        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.created_by = request.user
            order.save()
            
            formset.instance = order
            formset.save()
            
            messages.success(request, 'Order created successfully!')
            return redirect('order_detail', pk=order.pk)
    else:
        order_form = OrderForm()
        formset = OrderItemFormSet()
    
    return render(request, 'orders/create.html', {
        'order_form': order_form,
        'formset': formset
    })

# Dynamic form processing
class DynamicSearchForm(forms.Form):
    SEARCH_FIELDS = [
        ('name', 'Product Name'),
        ('category', 'Category'),
        ('price', 'Price'),
        ('description', 'Description'),
    ]
    
    search_field = forms.ChoiceField(choices=SEARCH_FIELDS)
    search_query = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
    
    def search_products(self):
        if not self.is_valid():
            return Product.objects.none()
        
        cleaned_data = self.cleaned_data
        queryset = Product.objects.all()
        
        # Dynamic filtering based on form data
        search_field = cleaned_data.get('search_field')
        search_query = cleaned_data.get('search_query')
        
        if search_query:
            if search_field == 'name':
                queryset = queryset.filter(name__icontains=search_query)
            elif search_field == 'category':
                queryset = queryset.filter(category__name__icontains=search_query)
            elif search_field == 'description':
                queryset = queryset.filter(description__icontains=search_query)
        
        # Price range filtering
        min_price = cleaned_data.get('min_price')
        max_price = cleaned_data.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        return queryset

# AJAX form processing
def ajax_contact_form(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save to database or send email
            ContactSubmission.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message!'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors.get_json_data()
            })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
```

This comprehensive Week 9 module covers Django templates and forms in depth, providing students with the knowledge needed to create dynamic, interactive web applications with robust form handling and template systems.
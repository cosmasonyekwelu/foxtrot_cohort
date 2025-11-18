# Django Web Development Course - Week 7: Django and REST APIs

## Course Description
This course provides a comprehensive introduction to Django, a high-level Python web framework that enables rapid development of secure and maintainable websites. Students will learn to build dynamic web applications from scratch using Django's powerful components and best practices.

## Module 1: Similarities between Python Dictionaries and JS Objects

### Understanding Data Structures

```python
# Python Dictionary Examples
python_dict = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "is_active": True,
    "hobbies": ["reading", "gaming", "coding"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zipcode": "10001"
    },
    "scores": {
        "math": 95,
        "science": 88,
        "history": 92
    }
}

# Accessing dictionary values
name = python_dict["name"]
age = python_dict.get("age")
city = python_dict["address"]["city"]

# Modifying dictionaries
python_dict["age"] = 31
python_dict["phone"] = "+1234567890"  # Add new key
del python_dict["is_active"]  # Remove key

# Dictionary methods
keys = python_dict.keys()
values = python_dict.values()
items = python_dict.items()
```

```javascript
// JavaScript Object Examples
const jsObject = {
    name: "John Doe",
    age: 30,
    email: "john@example.com",
    isActive: true,
    hobbies: ["reading", "gaming", "coding"],
    address: {
        street: "123 Main St",
        city: "New York",
        zipcode: "10001"
    },
    scores: {
        math: 95,
        science: 88,
        history: 92
    }
};

// Accessing object values
const name = jsObject.name;
const age = jsObject["age"];
const city = jsObject.address.city;

// Modifying objects
jsObject.age = 31;
jsObject.phone = "+1234567890";  // Add new property
delete jsObject.isActive;  // Remove property

// Object methods
const keys = Object.keys(jsObject);
const values = Object.values(jsObject);
const entries = Object.entries(jsObject);
```

### Key Similarities and Differences

```python
# Comparison table in code comments
"""
Feature              Python Dictionary      JavaScript Object
-------------        -----------------      -----------------
Creation             {key: value}           {key: value} or new Object()
Access               dict["key"]            obj.key or obj["key"]
Nested Access        dict["a"]["b"]         obj.a.b or obj["a"]["b"]
Check key exists     "key" in dict          "key" in obj
Get all keys         dict.keys()            Object.keys(obj)
Get all values       dict.values()          Object.values(obj)
Get key-value pairs  dict.items()           Object.entries(obj)
Add/Modify           dict["new"] = value    obj.new = value
Delete key           del dict["key"]        delete obj.key
Size                 len(dict)              Object.keys(obj).length
"""

# Practical conversion examples
def python_to_js_compatible(data):
    """Convert Python data types to JSON-compatible formats"""
    if isinstance(data, dict):
        return {str(key): python_to_js_compatible(value) 
                for key, value in data.items()}
    elif isinstance(data, (list, tuple)):
        return [python_to_js_compatible(item) for item in data]
    elif isinstance(data, (int, float, str, bool, type(None))):
        return data
    else:
        return str(data)  # Convert other types to string

# Example usage
python_data = {
    "user_id": 12345,
    "username": "johndoe",
    "preferences": {"theme": "dark", "language": "en"},
    "created_at": "2023-01-01T10:30:00"  # datetime would need conversion
}

js_compatible_data = python_to_js_compatible(python_data)
```

## Module 2: Preparing JSON Responses

### Manual JSON Responses in Django

```python
# Basic JSON responses
from django.http import JsonResponse
from django.core.serializers import serialize
import json

def basic_json_response(request):
    # Simple dictionary response
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "data": {
            "users": [
                {"id": 1, "name": "John Doe", "email": "john@example.com"},
                {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
            ],
            "total_count": 2
        }
    }
    return JsonResponse(data)

def json_response_with_models(request):
    from myapp.models import User, Product
    
    # Convert model instances to dictionaries manually
    users = User.objects.all()[:5]
    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "date_joined": user.date_joined.isoformat()
        })
    
    response_data = {
        "users": user_list,
        "count": len(user_list)
    }
    return JsonResponse(response_data)

def json_response_advanced(request):
    # Custom JSON response with status codes
    try:
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse(
                {"error": "user_id parameter is required"}, 
                status=400
            )
        
        user = User.objects.get(id=user_id)
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "profile": {
                "first_name": user.first_name,
                "last_name": user.last_name
            }
        }
        
        return JsonResponse({
            "status": "success",
            "data": user_data
        })
        
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, 
            status=404
        )
    except Exception as e:
        return JsonResponse(
            {"error": "Internal server error"}, 
            status=500
        )
```

### Advanced JSON Response Techniques

```python
# Custom JSON encoder for complex types
import json
from datetime import datetime, date
from decimal import Decimal
from django.db import models

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, models.Model):
            # Convert model instance to dictionary
            return self.model_to_dict(obj)
        elif isinstance(obj, models.QuerySet):
            return [self.model_to_dict(item) for item in obj]
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)
    
    def model_to_dict(self, obj):
        """Convert model instance to dictionary"""
        data = {}
        for field in obj._meta.fields:
            value = getattr(obj, field.name)
            if isinstance(value, (datetime, date)):
                data[field.name] = value.isoformat()
            elif isinstance(value, Decimal):
                data[field.name] = float(value)
            else:
                data[field.name] = value
        return data

def custom_json_response(request):
    from myapp.models import Order, Product
    
    # Complex data with custom types
    order = Order.objects.first()
    products = Product.objects.filter(available=True)
    
    data = {
        "order": order,  # Model instance
        "products": products,  # QuerySet
        "timestamp": datetime.now(),  # DateTime
        "metadata": {
            "version": "1.0",
            "total_value": Decimal('999.99')
        }
    }
    
    json_string = json.dumps(data, cls=CustomJSONEncoder, indent=2)
    return HttpResponse(json_string, content_type='application/json')

# JSON response with pagination
from django.core.paginator import Paginator

def paginated_json_response(request):
    from myapp.models import Product
    
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    
    products = Product.objects.all().order_by('name')
    paginator = Paginator(products, page_size)
    
    try:
        page = paginator.page(page_number)
    except:
        return JsonResponse({"error": "Invalid page number"}, status=400)
    
    product_list = []
    for product in page.object_list:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
            "category": product.category.name
        })
    
    response_data = {
        "products": product_list,
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_next": page.has_next(),
            "has_previous": page.has_previous(),
            "page_size": page_size
        }
    }
    
    return JsonResponse(response_data)
```

## Module 3: Django REST Framework

### Introduction to Django REST Framework (DRF)

```python
# Installation and setup
"""
Install DRF:
pip install djangorestframework

Add to INSTALLED_APPS in settings.py:
INSTALLED_APPS = [
    ...
    'rest_framework',
]

Configure DRF in settings.py:
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
"""

# Basic serializers
from rest_framework import serializers
from myapp.models import Product, Category, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category', 
        write_only=True
    )
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 
            'category', 'category_id', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value

class UserSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'products']
```

### DRF Views and Viewsets

```python
# API Views with DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        """Get all products"""
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        })
    
    def post(self, request):
        """Create a new product"""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
    
    def get(self, request, pk):
        """Get single product"""
        product = self.get_object(pk)
        if product is None:
            return Response(
                {"error": "Product not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """Update product"""
        product = self.get_object(pk)
        if product is None:
            return Response(
                {"error": "Product not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete product"""
        product = self.get_object(pk)
        if product is None:
            return Response(
                {"error": "Product not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### ViewSets and Routers

```python
# Using ViewSets for CRUD operations
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        """Optionally filter products by category"""
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Custom action to get featured products"""
        featured_products = self.get_queryset().filter(featured=True)
        serializer = self.get_serializer(featured_products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def set_featured(self, request, pk=None):
        """Custom action to set product as featured"""
        product = self.get_object()
        product.featured = True
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# URL configuration with routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),  # For browsable API login
]
```

## Module 4: Using the Django Admin Interface

### Admin Interface Overview

```python
# Basic admin configuration
from django.contrib import admin
from myapp.models import Product, Category, Order, OrderItem

# Basic model registration
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

# Custom admin classes
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = ['name', 'price', 'category', 'created_at', 'available']
    
    # Add filters in the sidebar
    list_filter = ['category', 'available', 'created_at']
    
    # Add search functionality
    search_fields = ['name', 'description']
    
    # Prepopulate slug field from name
    prepopulated_fields = {'slug': ('name',)}
    
    # Fields to display in edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'category')
        }),
        ('Pricing and Inventory', {
            'fields': ('price', 'stock_quantity', 'available')
        }),
        ('Additional Information', {
            'fields': ('featured_image', 'tags'),
            'classes': ('collapse',)  # Collapsible section
        })
    )
    
    # Inline editing for related models
    class OrderItemInline(admin.TabularInline):
        model = OrderItem
        extra = 1  # Number of empty forms to display
    
    # Actions for bulk operations
    actions = ['make_available', 'make_unavailable']
    
    def make_available(self, request, queryset):
        queryset.update(available=True)
    make_available.short_description = "Mark selected products as available"
    
    def make_unavailable(self, request, queryset):
        queryset.update(available=False)
    make_unavailable.short_description = "Mark selected products as unavailable"
```

### Advanced Admin Customization

```python
# Advanced admin configurations
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'customer', 'total_amount', 'status', 
        'created_at', 'updated_at'
    ]
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['customer__username', 'customer__email']
    readonly_fields = ['created_at', 'updated_at', 'total_amount']
    
    # Custom method in list display
    def total_amount(self, obj):
        return f"${obj.calculate_total():.2f}"
    total_amount.short_description = 'Total Amount'
    
    # Fields organization
    fieldsets = (
        ('Order Information', {
            'fields': ('customer', 'status', 'shipping_address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Inline editing for order items
    inlines = [OrderItemInline]
    
    # Date hierarchy for navigation
    date_hierarchy = 'created_at'
    
    # Custom change list view
    def changelist_view(self, request, extra_context=None):
        # Add custom context data
        extra_context = extra_context or {}
        extra_context['total_orders'] = Order.objects.count()
        extra_context['pending_orders'] = Order.objects.filter(status='pending').count()
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_count', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Number of Products'

# Custom admin site configuration
class CustomAdminSite(admin.AdminSite):
    site_header = "My E-commerce Administration"
    site_title = "E-commerce Admin Portal"
    index_title = "Welcome to E-commerce Admin"

custom_admin_site = CustomAdminSite(name='custom_admin')

# Register models with custom admin site
custom_admin_site.register(Product, ProductAdmin)
custom_admin_site.register(Category, CategoryAdmin)
```

## Module 5: Enabling the Admin Interface

### Admin Setup and Configuration

```python
# URLs configuration for admin
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # or for custom admin site:
    # path('admin/', custom_admin_site.urls),
]

# Admin site configuration
admin.site.site_header = "My Django Project Administration"
admin.site.site_title = "Django Project Admin Portal"
admin.site.index_title = "Welcome to Django Project Admin"

# Customizing admin authentication
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms

class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and not username.endswith('@mycompany.com'):
            raise forms.ValidationError(
                "Only company email addresses are allowed for admin access."
            )
        return username

# Apply custom form (in urls.py or admin.py)
admin.site.login_form = CustomAdminAuthenticationForm

# Admin site documentation
"""
To enable admin documentation:
1. Add 'django.contrib.admindocs' to INSTALLED_APPS
2. Include in urls.py: path('admin/doc/', include('django.contrib.admindocs.urls'))
3. Install docutils: pip install docutils
"""

# Admin static files configuration
"""
Make sure static files are configured in settings.py:

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

Then run: python manage.py collectstatic
"""
```

### Security and Permissions

```python
# Admin security configurations
from django.contrib.admin import AdminSite
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

class SecureAdminSite(AdminSite):
    # Require login for all admin pages
    @never_cache
    def login(self, request, extra_context=None):
        return super().login(request, extra_context)
    
    # Custom permission checks
    def has_permission(self, request):
        return (
            request.user.is_active and
            request.user.is_staff and
            request.user.is_superuser  # Only superusers can access
        )

secure_admin_site = SecureAdminSite(name='secure_admin')

# Custom admin permissions
@admin.register(Product)
class SecureProductAdmin(admin.ModelAdmin):
    # Restrict access based on permissions
    def has_add_permission(self, request):
        return request.user.has_perm('myapp.add_product')
    
    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('myapp.change_product')
    
    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('myapp.delete_product')
    
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('myapp.view_product')
    
    # Custom queryset based on user permissions
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

# Admin log entries
from django.contrib.admin.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_repr', 'action_flag']
    list_filter = ['action_time', 'user', 'content_type']
    search_fields = ['object_repr', 'user__username']
    date_hierarchy = 'action_time'
    
    def has_add_permission(self, request):
        return False  # Log entries are created automatically
    
    def has_change_permission(self, request, obj=None):
        return False  # Log entries should not be modified
```

## Module 6: Creating an Admin User

### Admin User Management

```bash
# Creating admin users from command line
python manage.py createsuperuser

# Interactive creation process:
"""
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
"""

# Non-interactive creation (for scripts)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password123')" | python manage.py shell

# Creating multiple admin users programmatically
python manage.py shell
```

```python
# Programmatic admin user creation
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create initial admin users'
    
    def handle(self, *args, **options):
        User = get_user_model()
        
        # Check if admin user already exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully created admin user')
            )
        else:
            self.stdout.write('Admin user already exists')
        
        # Create additional staff users
        staff_users = [
            {'username': 'manager', 'email': 'manager@example.com', 'password': 'manager123'},
            {'username': 'editor', 'email': 'editor@example.com', 'password': 'editor123'},
        ]
        
        for user_data in staff_users:
            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password'],
                    is_staff=True,
                    is_superuser=False
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created staff user: {user_data["username"]}')
                )

# User profile model with admin integration
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"

# Inline admin for user profiles
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Custom User admin
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Custom actions
    actions = ['activate_users', 'deactivate_users']
    
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
    activate_users.short_description = "Activate selected users"
    
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_users.short_description = "Deactivate selected users"

# Unregister default User admin and register custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
```

### Advanced Admin User Features

```python
# Custom user model with enhanced admin features
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields
    phone_number = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    
    # Custom permissions
    class Meta:
        permissions = [
            ("can_export_data", "Can export data"),
            ("can_import_data", "Can import data"),
            ("can_manage_users", "Can manage users"),
        ]
    
    def __str__(self):
        return f"{self.username} ({self.email})"

# Admin for custom user model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'email', 'first_name', 'last_name', 
        'company', 'is_staff', 'is_active', 'date_joined'
    ]
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'company', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'company']
    readonly_fields = ['last_login', 'date_joined']
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'company', 'bio', 'avatar')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    # Custom admin actions
    actions = ['export_user_data', 'send_welcome_email']
    
    def export_user_data(self, request, queryset):
        # Implementation for exporting user data
        from django.http import HttpResponse
        import csv
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Username', 'Email', 'First Name', 'Last Name', 'Company'])
        
        for user in queryset:
            writer.writerow([user.username, user.email, user.first_name, user.last_name, user.company])
        
        return response
    export_user_data.short_description = "Export selected users to CSV"
    
    def send_welcome_email(self, request, queryset):
        # Implementation for sending welcome emails
        from django.core.mail import send_mail
        from django.conf import settings
        
        for user in queryset:
            if user.email:
                send_mail(
                    'Welcome to Our Platform',
                    f'Hello {user.first_name or user.username}, welcome to our platform!',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,
                )
        
        self.message_user(request, f"Welcome emails sent to {queryset.count()} users.")
    send_welcome_email.short_description = "Send welcome email to selected users"

# Update settings.py to use custom user model
"""
AUTH_USER_MODEL = 'myapp.CustomUser'
"""
```

This comprehensive Week 7 module covers Django REST APIs and Admin Interface in depth, providing students with the knowledge needed to build robust APIs and manage application data effectively through Django's powerful admin interface.
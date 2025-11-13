from django.urls import path
from market import views

urlpatterns = [
    path('product/', views.get_product, name='get-product'),
]

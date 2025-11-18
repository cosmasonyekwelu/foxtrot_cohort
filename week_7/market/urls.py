from django.urls import path
from market import views

urlpatterns = [
    path('get_product/', views.get_product, name='get-product'),
]

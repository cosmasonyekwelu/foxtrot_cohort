from django.urls import path
from market import views

urlpatterns = [
    path('get_product/', views.get_product, name='get-product'),
    path('create_product/', views.create_product, name='create-product'),
    path('update_product/<int:id>/', views.update_product, name='update-product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete-product'),
]

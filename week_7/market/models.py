from django.db import models


# A Django project and app are needed before defining any models.
# After starting an app, models can be created in the file app_name/models.py.

# Create your models here.
class Market_Product(models.Model):
    CATEGORY_CHOICES = (
        ("accessories", "Accessories"),
        ("fashion", "Fashion"),
        ("electronics", "Electronics"),
    )
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

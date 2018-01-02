from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    photo_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

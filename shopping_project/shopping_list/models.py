from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    is_bought = models.BooleanField(default=False)

    def __str__(self):
        return self.name
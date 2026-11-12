from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    is_bought = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Przypisanie do użytkownika
    title = models.CharField(max_length=200, verbose_name="Tytuł wydarzenia")
    description = models.TextField(blank=True, verbose_name="Opis")
    date = models.DateField(verbose_name="Data wydarzenia")

    def __str__(self):
        return self.title
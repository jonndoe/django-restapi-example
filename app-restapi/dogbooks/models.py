from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Dogbook(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
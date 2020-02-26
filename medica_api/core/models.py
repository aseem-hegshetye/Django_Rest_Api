from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50,default=None, null=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.first_name
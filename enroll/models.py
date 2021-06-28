from django.db import models


class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=100)
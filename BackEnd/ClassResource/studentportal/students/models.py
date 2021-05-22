from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    varsity_id = models.CharField(max_length=20, unique=True)
    blood_group = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

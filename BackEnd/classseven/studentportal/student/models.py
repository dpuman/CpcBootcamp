from django.db import models

# Create your models here.


class student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.FloatField()
    section = models.CharField(max_length=4)
    gender = models.CharField(max_length=5)

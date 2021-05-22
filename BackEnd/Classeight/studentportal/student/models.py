from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    student_id = models.IntegerField()
    cgpa = models.FloatField()


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    courses = models.CharField(max_length=50)


class Courses(models.Model):
    name = models.CharField(max_length=50)

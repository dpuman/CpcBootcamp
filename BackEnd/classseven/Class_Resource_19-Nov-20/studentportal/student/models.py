from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    varsity_id = models.IntegerField()
    age = models.FloatField()
    section = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=20)



# Model, IntegerField, CharField, FloatField


# class Human():
#     hand = 2
#     leg = 2
#     hair_color = None


# class Bangladeshi(Human):


# class American(Human):


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    TYPE_CHOICES = [
        ('category', 'Category'),
        ('subcategory', 'Subcategory'),
        ('tag', 'Tag'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.TextField()
    at_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blogs')
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.title

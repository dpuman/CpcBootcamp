from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    new_product = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class GetInTouch(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.first_name

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50,)
    price = models.FloatField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name

# Generated by Django 3.1.5 on 2021-02-15 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0006_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='expire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

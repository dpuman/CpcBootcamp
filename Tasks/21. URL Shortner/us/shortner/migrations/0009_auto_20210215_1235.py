# Generated by Django 3.1.5 on 2021-02-15 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0008_auto_20210215_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='expire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 17, 12, 35, 10, 146888)),
        ),
    ]

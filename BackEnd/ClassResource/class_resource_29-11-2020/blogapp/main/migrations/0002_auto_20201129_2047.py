# Generated by Django 3.0.7 on 2020-11-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='main.Comment'),
        ),
    ]
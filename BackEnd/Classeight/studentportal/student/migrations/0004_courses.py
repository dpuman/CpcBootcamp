# Generated by Django 3.1.2 on 2020-11-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]

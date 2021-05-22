# Generated by Django 3.1.5 on 2021-01-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmasite', '0002_getintouct'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='GetInTouct',
        ),
    ]
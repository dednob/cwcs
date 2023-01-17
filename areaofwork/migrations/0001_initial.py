# Generated by Django 4.1.1 on 2023-01-17 09:30

import areaofwork.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areaofwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('details', models.TextField()),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('image', models.ImageField(null=True, upload_to=areaofwork.models.generate_filename)),
            ],
        ),
    ]

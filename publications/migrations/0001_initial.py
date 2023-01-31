# Generated by Django 4.1.1 on 2023-01-31 21:52

from django.db import migrations, models
import publications.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(null=True, upload_to=publications.models.generate_filename)),
            ],
        ),
    ]
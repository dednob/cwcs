# Generated by Django 4.1.1 on 2023-02-01 09:41

from django.db import migrations, models
import publications.models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publications_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='book_banner_image',
            field=models.ImageField(null=True, upload_to=publications.models.generate_imagename),
        ),
        migrations.AddField(
            model_name='publications',
            name='paper_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
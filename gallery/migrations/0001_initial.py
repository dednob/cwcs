# Generated by Django 4.1.1 on 2023-01-17 09:30

from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('details', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=500, null=True, unique=True)),
                ('image', models.ImageField(null=True, upload_to=gallery.models.generate_filename)),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='projects.projects')),
            ],
        ),
    ]
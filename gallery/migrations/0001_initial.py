# Generated by Django 4.1.1 on 2023-01-26 07:17

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
                ('image', models.ImageField(null=True, upload_to=gallery.models.generate_filename)),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='projects.projects')),
            ],
        ),
    ]

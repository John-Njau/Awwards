# Generated by Django 4.0.5 on 2022-06-12 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0010_profile_created_at_project_uploaded_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='created_at',
        ),
    ]
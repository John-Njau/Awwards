# Generated by Django 4.0.5 on 2022-06-12 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_ratings_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]

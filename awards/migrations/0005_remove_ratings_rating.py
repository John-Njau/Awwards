# Generated by Django 4.0.5 on 2022-06-13 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_ratings_average_rating_ratings_content_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='rating',
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
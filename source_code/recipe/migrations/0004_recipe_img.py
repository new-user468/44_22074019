# Generated by Django 3.2.6 on 2021-11-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20211101_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='recipe_imgs'),
        ),
    ]
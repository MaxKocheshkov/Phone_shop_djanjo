# Generated by Django 2.2.10 on 2020-08-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20200806_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(),
        ),
    ]
# Generated by Django 3.2.23 on 2023-11-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20231112_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='block',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='confirmation_code',
            field=models.CharField(default=84713, max_length=5),
        ),
    ]

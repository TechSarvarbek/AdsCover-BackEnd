# Generated by Django 3.2.23 on 2023-11-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_users_confirmation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='block',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='confirmation_code',
            field=models.CharField(default=31730, max_length=5),
        ),
    ]

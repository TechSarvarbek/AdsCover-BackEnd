# Generated by Django 3.2.23 on 2023-11-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20231109_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='status',
        ),
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

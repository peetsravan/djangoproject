# Generated by Django 5.2.3 on 2025-06-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='app_category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='apps',
            name='sub_category',
            field=models.CharField(max_length=20),
        ),
    ]

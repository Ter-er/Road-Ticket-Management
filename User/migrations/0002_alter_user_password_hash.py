# Generated by Django 5.1.1 on 2024-09-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(max_length=128),
        ),
    ]

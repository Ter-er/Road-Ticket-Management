# Generated by Django 5.1.1 on 2024-09-24 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 9, 10, 2, 13, 543826, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-21 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_alter_payment_payment_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 6, 13, 43, 39, 24416, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-24 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0003_alter_payment_payment_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 9, 10, 9, 50, 548302, tzinfo=datetime.timezone.utc)),
        ),
    ]

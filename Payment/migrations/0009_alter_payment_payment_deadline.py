# Generated by Django 5.1.1 on 2024-09-23 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0008_alter_payment_payment_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 8, 14, 18, 3, 877561, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_no',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]

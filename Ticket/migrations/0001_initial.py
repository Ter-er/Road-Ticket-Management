# Generated by Django 5.1.1 on 2024-09-24 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Offense', '0001_initial'),
        ('User', '0001_initial'),
        ('Vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_no', models.CharField(blank=True, max_length=20, unique=True)),
                ('ticket_image', models.ImageField(blank=True, null=True, upload_to='ticket_images/')),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('official_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending', max_length=10)),
                ('penalty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Offense.offense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicle')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-21 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_date', models.DateTimeField(auto_now_add=True)),
                ('proof_image', models.ImageField(blank=True, null=True, upload_to='proof_images/')),
                ('proof_video', models.FileField(blank=True, null=True, upload_to='proof_videos/')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket.ticket')),
            ],
        ),
    ]
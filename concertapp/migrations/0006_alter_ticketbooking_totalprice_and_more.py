# Generated by Django 5.0.1 on 2025-01-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0005_ticketbooking_totalprice_ticketbooking_useremail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketbooking',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='useremail',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]

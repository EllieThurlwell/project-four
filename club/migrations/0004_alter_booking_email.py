# Generated by Django 3.2 on 2021-12-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_remove_booking_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

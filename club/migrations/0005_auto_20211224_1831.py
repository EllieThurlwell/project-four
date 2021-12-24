# Generated by Django 3.2 on 2021-12-24 18:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_alter_booking_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lname',
        ),
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-09-11 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pynetsoftwares', '0007_addpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addpage',
            old_name='slug',
            new_name='pageslug',
        ),
    ]
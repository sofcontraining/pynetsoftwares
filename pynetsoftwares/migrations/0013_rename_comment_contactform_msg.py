# Generated by Django 3.2.5 on 2021-09-13 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pynetsoftwares', '0012_contactform_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='comment',
            new_name='msg',
        ),
    ]

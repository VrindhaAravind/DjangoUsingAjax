# Generated by Django 3.2.5 on 2021-10-04 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update_user', '0002_auto_20211001_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='user',
        ),
    ]

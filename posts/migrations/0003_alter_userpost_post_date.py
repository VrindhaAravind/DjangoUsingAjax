# Generated by Django 3.2.5 on 2021-10-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_userpost_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

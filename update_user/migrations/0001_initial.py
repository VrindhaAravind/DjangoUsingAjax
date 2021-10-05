# Generated by Django 3.2.5 on 2021-09-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=15)),
                ('dob', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-31 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_venue_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='owner',
        ),
    ]
# Generated by Django 3.2.9 on 2022-03-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_events_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(blank=True, default=1, verbose_name='Venue Owner'),
        ),
    ]

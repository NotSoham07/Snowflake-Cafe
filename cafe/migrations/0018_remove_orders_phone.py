# Generated by Django 3.1.3 on 2020-11-29 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0017_auto_20201129_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone',
        ),
    ]
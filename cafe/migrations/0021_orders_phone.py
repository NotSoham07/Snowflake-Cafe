# Generated by Django 3.1.3 on 2020-11-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0020_remove_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]

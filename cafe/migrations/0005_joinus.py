# Generated by Django 3.1.1 on 2020-10-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_auto_20201010_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joinus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.IntegerField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('file', models.FileField(default='', upload_to='shop/files')),
                ('subject', models.CharField(max_length=300)),
            ],
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-08 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0011_auto_20190903_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.CharField(max_length=11),
        ),
    ]
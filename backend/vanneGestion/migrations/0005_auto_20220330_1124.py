# Generated by Django 3.1 on 2022-03-30 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanneGestion', '0004_auto_20220330_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vannes',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2080, 5, 17, 0, 0)),
        ),
        migrations.AlterField(
            model_name='vannes',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2080, 5, 17, 0, 0)),
        ),
    ]

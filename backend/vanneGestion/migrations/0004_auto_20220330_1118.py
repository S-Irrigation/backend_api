# Generated by Django 3.1 on 2022-03-30 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanneGestion', '0003_auto_20220323_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vannes',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2080, 5, 17, 0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='vannes',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2080, 5, 17, 0, 0), null=True),
        ),
    ]

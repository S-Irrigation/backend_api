# Generated by Django 3.1 on 2022-04-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanneGestion', '0012_auto_20220404_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vannes',
            name='end',
            field=models.DateTimeField(default='2022-04-04 17:55:05'),
        ),
        migrations.AlterField(
            model_name='vannes',
            name='start',
            field=models.DateTimeField(default='2022-04-04 17:55:05'),
        ),
    ]
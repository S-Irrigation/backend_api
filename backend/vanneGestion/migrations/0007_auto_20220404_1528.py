# Generated by Django 3.1 on 2022-04-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanneGestion', '0006_auto_20220404_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vannes',
            name='end',
            field=models.DateTimeField(default='2022-04-04 15:28:10'),
        ),
        migrations.AlterField(
            model_name='vannes',
            name='start',
            field=models.DateTimeField(default='2022-04-04 15:28:10'),
        ),
    ]
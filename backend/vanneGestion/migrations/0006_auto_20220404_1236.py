# Generated by Django 3.1 on 2022-04-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanneGestion', '0005_auto_20220330_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vannes',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vannes',
            name='end',
            field=models.DateTimeField(default='2022-04-04 12:36:30'),
        ),
        migrations.AlterField(
            model_name='vannes',
            name='start',
            field=models.DateTimeField(default='2022-04-04 12:36:30'),
        ),
    ]
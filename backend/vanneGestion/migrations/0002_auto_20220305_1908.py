# Generated by Django 3.1 on 2022-03-05 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vanneGestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capteur',
            name='champ',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='vanneGestion.champ'),
        ),
        migrations.AddField(
            model_name='vanne',
            name='champ',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='vanneGestion.champ'),
        ),
    ]

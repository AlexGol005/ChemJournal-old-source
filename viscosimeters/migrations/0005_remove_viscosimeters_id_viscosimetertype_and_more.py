# Generated by Django 4.0.4 on 2022-04-28 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viscosimeters', '0004_remove_viscosimeters_diameter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viscosimeters',
            name='id_ViscosimeterType',
        ),
        migrations.AddField(
            model_name='viscosimeters',
            name='viscosity1000',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='viscosimeters.viscosimetertype', verbose_name='Вязкость за 1000 сек'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-28 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viscosimeters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viscosimeters',
            name='companyName',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='viscosimeters.manufacturer', verbose_name='Производитель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viscosimeters',
            name='status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='viscosimeters.status', verbose_name='Статус'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='Creado'),
        ),
        migrations.AddField(
            model_name='factura',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='Creado'),
        ),
        migrations.AddField(
            model_name='marca',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='Creado'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='Creado'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='its_cpv',
            field=models.BooleanField(verbose_name='¿La ubicacion es CPV?'),
        ),
    ]
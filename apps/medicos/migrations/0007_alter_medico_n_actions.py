# Generated by Django 5.0.3 on 2024-04-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0006_medico_is_actionist_medico_n_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='n_actions',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Número de acciones'),
        ),
    ]

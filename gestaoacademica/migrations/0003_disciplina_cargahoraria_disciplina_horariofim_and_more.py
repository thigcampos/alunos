# Generated by Django 5.0.6 on 2024-06-11 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoacademica', '0002_disciplina_diadasemana'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='cargaHoraria',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='horarioFim',
            field=models.TimeField(default=datetime.datetime(2024, 6, 11, 16, 22, 31, 445491)),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='horarioInicio',
            field=models.TimeField(default=datetime.datetime(2024, 6, 11, 16, 22, 31, 445449)),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='numeroDeaulas',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='diaDaSemana',
            field=models.TextField(choices=[('DOMINGO', 'Domingo'), ('SEGUNDA', 'Segunda-feira'), ('TERCA', 'Terça-feira'), ('QUARTA', 'Quarta-feira'), ('QUINTA', 'Quinta-feira'), ('SEXTA', 'Sexta-feira'), ('SABADO', 'Sábado')]),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoacademica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='diaDaSemana',
            field=models.TextField(choices=[('DOMINGO', 'Domingo'), ('SEGUNDA', 'Segunda-feira'), ('TERCA', 'Terça-feira'), ('QUARTA', 'Quarta-feira'), ('QUINTA', 'Quinta-feira'), ('SEXTA', 'Sexta-feira'), ('SABADO', 'Sábado')], default=''),
        ),
    ]

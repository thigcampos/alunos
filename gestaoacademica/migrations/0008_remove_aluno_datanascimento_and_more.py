# Generated by Django 5.0.6 on 2024-06-11 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestaoacademica", "0007_alter_disciplina_horariofim_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aluno",
            name="dataNascimento",
        ),
        migrations.AlterField(
            model_name="disciplina",
            name="horarioFim",
            field=models.TimeField(default=datetime.time(20, 55, 41, 357611)),
        ),
        migrations.AlterField(
            model_name="disciplina",
            name="horarioInicio",
            field=models.TimeField(default=datetime.time(20, 55, 41, 357566)),
        ),
    ]
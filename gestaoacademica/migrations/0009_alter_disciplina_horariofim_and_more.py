# Generated by Django 5.0.6 on 2024-06-12 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestaoacademica", "0008_remove_aluno_datanascimento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disciplina",
            name="horarioFim",
            field=models.TimeField(default=datetime.time(8, 28, 25, 489477)),
        ),
        migrations.AlterField(
            model_name="disciplina",
            name="horarioInicio",
            field=models.TimeField(default=datetime.time(8, 28, 25, 489458)),
        ),
    ]

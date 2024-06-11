# Generated by Django 5.0.6 on 2024-06-11 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "gestaoacademica",
            "0003_disciplina_cargahoraria_disciplina_horariofim_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="disciplina",
            name="horarioFim",
            field=models.TimeField(default=datetime.time(16, 24, 38, 633380)),
        ),
        migrations.AlterField(
            model_name="disciplina",
            name="horarioInicio",
            field=models.TimeField(default=datetime.time(16, 24, 38, 633350)),
        ),
    ]

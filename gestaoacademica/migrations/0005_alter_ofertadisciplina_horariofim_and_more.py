# Generated by Django 5.0.6 on 2024-06-15 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestaoacademica", "0004_alter_ofertadisciplina_horariofim_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ofertadisciplina",
            name="horarioFim",
            field=models.TimeField(default=datetime.time(16, 23, 10, 77208)),
        ),
        migrations.AlterField(
            model_name="ofertadisciplina",
            name="horarioInicio",
            field=models.TimeField(default=datetime.time(16, 23, 10, 77178)),
        ),
    ]

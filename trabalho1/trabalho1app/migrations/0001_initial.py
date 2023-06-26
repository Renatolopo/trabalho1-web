# Generated by Django 4.2.1 on 2023-06-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "periodo_ingresso",
                    models.CharField(max_length=100, verbose_name="Nome"),
                ),
                ("nota", models.IntegerField(max_length=100, verbose_name="Nota")),
                ("situacao", models.CharField(max_length=100, verbose_name="Situação")),
            ],
        ),
    ]

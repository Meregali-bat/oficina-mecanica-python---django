# Generated by Django 4.2.7 on 2023-11-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nome", models.CharField(max_length=100)),
                ("sobrenome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=255)),
                ("cpf", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="Carro",
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
                ("carro", models.CharField(max_length=100)),
                ("placa", models.CharField(max_length=8)),
                ("ano", models.IntegerField(max_length=4)),
                ("consertos", models.IntegerField(default=0)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.cliente",
                    ),
                ),
            ],
        ),
    ]
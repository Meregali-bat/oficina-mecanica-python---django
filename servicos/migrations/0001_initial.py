# Generated by Django 4.2.4 on 2023-12-04 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pecas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Servico",
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
                ("nome", models.CharField(max_length=200)),
                ("valor", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "peca",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pecas.peca",
                    ),
                ),
            ],
        ),
    ]

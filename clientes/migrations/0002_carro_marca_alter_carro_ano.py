# Generated by Django 4.2.4 on 2023-12-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carro",
            name="marca",
            field=models.CharField(default="temp", max_length=100),
        ),
        migrations.AlterField(
            model_name="carro",
            name="ano",
            field=models.IntegerField(),
        ),
    ]
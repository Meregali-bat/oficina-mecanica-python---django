# Generated by Django 4.2.4 on 2023-12-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clientes", "0002_carro_marca_alter_carro_ano"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carro",
            name="marca",
            field=models.CharField(max_length=100),
        ),
    ]

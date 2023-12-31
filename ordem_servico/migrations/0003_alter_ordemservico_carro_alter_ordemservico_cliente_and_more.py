# Generated by Django 4.2.4 on 2023-12-04 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pecas", "0001_initial"),
        ("servicos", "0005_servico_descricao"),
        ("funcionarios", "0001_initial"),
        ("clientes", "0003_alter_carro_marca"),
        ("ordem_servico", "0002_alter_ordemservicopeca_quantidade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordemservico",
            name="carro",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clientes.carro",
            ),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clientes.cliente",
            ),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="data_conclusao",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="equipe",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="funcionarios.equipe",
            ),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="pecas",
            field=models.ManyToManyField(
                blank=True, through="ordem_servico.OrdemServicoPeca", to="pecas.peca"
            ),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="problema_carro",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="servicos",
            field=models.ManyToManyField(blank=True, to="servicos.servico"),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="valor_total_pecas",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="ordemservico",
            name="valor_total_servico",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=6, null=True
            ),
        ),
    ]

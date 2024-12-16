# Generated by Django 5.1.3 on 2024-12-06 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gerenciador_horario", "0010_alter_monday_client_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friday",
            name="id",
        ),
        migrations.RemoveField(
            model_name="thursday",
            name="id",
        ),
        migrations.RemoveField(
            model_name="tuesday",
            name="id",
        ),
        migrations.RemoveField(
            model_name="wednesday",
            name="id",
        ),
        migrations.AlterField(
            model_name="friday",
            name="client_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="friday",
            name="client_number",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="friday",
            name="horario",
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="thursday",
            name="client_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="thursday",
            name="client_number",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="thursday",
            name="horario",
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="tuesday",
            name="client_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="tuesday",
            name="client_number",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="tuesday",
            name="horario",
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="wednesday",
            name="client_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="wednesday",
            name="client_number",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="wednesday",
            name="horario",
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]

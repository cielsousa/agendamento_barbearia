# Generated by Django 5.1.3 on 2024-11-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador_horario', '0008_alter_monday_client_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monday',
            name='client_number',
            field=models.IntegerField(),
        ),
    ]

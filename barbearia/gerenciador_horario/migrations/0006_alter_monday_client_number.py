# Generated by Django 5.1.3 on 2024-11-22 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador_horario', '0005_alter_monday_client_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monday',
            name='client_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]

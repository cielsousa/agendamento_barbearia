# Generated by Django 5.1.3 on 2024-11-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador_horario', '0002_alter_friday_scheduled'),
    ]

    operations = [
        migrations.AddField(
            model_name='monday',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thursday',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tuesday',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wednesday',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
    ]

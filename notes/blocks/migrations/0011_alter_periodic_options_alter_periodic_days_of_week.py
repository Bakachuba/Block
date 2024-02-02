# Generated by Django 4.2.5 on 2024-02-01 14:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0010_alter_periodic_options_alter_periodic_days_of_week'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodic',
            options={'verbose_name': 'Периодическая задача', 'verbose_name_plural': 'Периодические задачи'},
        ),
        migrations.AlterField(
            model_name='periodic',
            name='days_of_week',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье'), ('weekdays', 'Будни'), ('weekends', 'Выходные'), ('every day', 'Каждый день')], default='every day', max_length=20), size=None),
        ),
    ]
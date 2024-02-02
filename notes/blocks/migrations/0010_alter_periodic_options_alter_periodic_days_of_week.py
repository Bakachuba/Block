# Generated by Django 4.2.5 on 2024-02-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0009_remove_periodic_next_execution_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodic',
            options={},
        ),
        migrations.AlterField(
            model_name='periodic',
            name='days_of_week',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье'), ('weekdays', 'Будни'), ('weekends', 'Выходные'), ('every day', 'Каждый день')], default='every day', max_length=20),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-16 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0004_idea'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'verbose_name': 'Идея', 'verbose_name_plural': 'Идеи'},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'verbose_name': 'Список', 'verbose_name_plural': 'Списки'},
        ),
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='periodic',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='summary',
            options={'verbose_name': 'Конспект', 'verbose_name_plural': 'Конспекты'},
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0006_alter_category_options_alter_periodic_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodic',
            name='next_execution_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodic',
            name='repetition_period',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodic',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

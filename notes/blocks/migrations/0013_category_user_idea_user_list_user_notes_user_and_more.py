# Generated by Django 4.2.5 on 2024-02-01 15:10

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blocks', '0012_alter_periodic_options_remove_periodic_time_period_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),

        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ForeignKey(default=get_user_model().objects.get(username='admin').id,
                                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),

        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(default=get_user_model().objects.get(username='admin').id,
                                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),

        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(default=get_user_model().objects.get(username='admin').id,
                                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),

        migrations.AddField(
            model_name='periodic',
            name='user',
            field=models.ForeignKey(default=get_user_model().objects.get(username='admin').id,
                                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),

        migrations.AddField(
            model_name='summary',
            name='user',
            field=models.ForeignKey(default=get_user_model().objects.get(username='admin').id,
                                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

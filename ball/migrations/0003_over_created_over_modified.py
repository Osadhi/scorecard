# Generated by Django 4.1.6 on 2023-03-04 05:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ball', '0002_alter_ball_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='over',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='over',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]

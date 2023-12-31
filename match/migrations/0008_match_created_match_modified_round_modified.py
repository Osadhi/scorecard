# Generated by Django 4.1.6 on 2023-03-03 10:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('match', '0007_match_slug_round_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='created',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='round',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]

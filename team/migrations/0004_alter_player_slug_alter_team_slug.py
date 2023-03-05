# Generated by Django 4.1.6 on 2023-03-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('team', '0003_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='slug'),
        ),
    ]

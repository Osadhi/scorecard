# Generated by Django 4.1.6 on 2023-03-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('match', '0012_alter_match_first_balling_alter_match_first_batting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]

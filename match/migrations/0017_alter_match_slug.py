# Generated by Django 4.1.6 on 2023-03-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('match', '0016_alter_match_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='slug',
            field=models.SlugField(
                blank=True, editable=False, unique=True, verbose_name='slug'),
        ),
    ]

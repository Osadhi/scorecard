# Generated by Django 4.1.6 on 2023-03-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('team', '0001_initial'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(to='team.team'),
        ),
    ]

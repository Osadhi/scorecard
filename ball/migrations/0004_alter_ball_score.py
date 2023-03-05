# Generated by Django 4.1.6 on 2023-03-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ball', '0003_over_created_over_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ball',
            name='score',
            field=models.CharField(
                choices=[('0', 'None'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                         ('7', '7')], default='0', max_length=1, verbose_name='score'),
        ),
    ]

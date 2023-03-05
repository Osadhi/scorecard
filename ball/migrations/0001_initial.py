# Generated by Django 4.1.6 on 2023-03-02 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('match', '0004_alter_match_first_balling_alter_match_first_batting_and_more'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Over',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.round')),
            ],
        ),
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wicket', models.BooleanField(default=False)),
                ('score',
                 models.CharField(choices=[('-', 'None'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('6', '6')],
                                  default='-', max_length=1, verbose_name='score')),
                ('ball', models.CharField(choices=[('-', 'Normal'), ('WB', 'Wide'), ('NB', 'No Ball'), ('B', 'Byes')],
                                          default='-', max_length=2, verbose_name='ball type')),
                ('batsman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
                ('over', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.over')),
            ],
        ),
    ]
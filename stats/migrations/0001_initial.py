# Generated by Django 4.1.6 on 2023-03-04 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('match', '0018_match_won'),
        ('team', '0009_alter_player_slug_alter_team_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='total')),
                ('wickets', models.IntegerField(blank=True, null=True, verbose_name='wickets')),
                ('overs', models.CharField(blank=True, max_length=10, null=True)),
                ('run_rate', models.FloatField(blank=True, null=True, verbose_name='run rate')),
                ('required_run_rate', models.FloatField(blank=True, null=True, verbose_name='required run rate')),
                ('extras', models.IntegerField(blank=True, null=True, verbose_name='extras')),
                ('remaining_balls', models.IntegerField(blank=True, null=True, verbose_name='remaining balls')),
                ('remaining_score', models.IntegerField(blank=True, null=True, verbose_name='remaining score')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerBatStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('balls', models.IntegerField(blank=True, null=True, verbose_name='balls')),
                ('runs', models.IntegerField(blank=True, null=True, verbose_name='runs')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerBallStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('wickets', models.IntegerField(blank=True, null=True, verbose_name='wickets')),
                ('overs', models.FloatField(blank=True, null=True, verbose_name='balls')),
                ('runs', models.IntegerField(blank=True, null=True, verbose_name='runs')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
            ],
        ),
    ]
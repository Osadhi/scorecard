# Generated by Django 4.1.6 on 2023-03-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('team', '0002_player_created_player_modified_player_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='team'),
        ),
    ]

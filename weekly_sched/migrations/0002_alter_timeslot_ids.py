# Generated by Django 5.1.2 on 2024-10-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekly_sched', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='ids',
            field=models.JSONField(default=dict),
        ),
    ]

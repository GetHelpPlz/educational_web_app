# Generated by Django 4.1.1 on 2022-11-29 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_counter_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='choice',
        ),
    ]

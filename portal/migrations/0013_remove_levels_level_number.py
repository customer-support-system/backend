# Generated by Django 5.0.2 on 2024-03-07 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_alter_issues_options_levels_level_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levels',
            name='level_number',
        ),
    ]
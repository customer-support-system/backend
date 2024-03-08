# Generated by Django 5.0.2 on 2024-02-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_rename_issue_id_solution_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Answered')], default=1),
        ),
    ]

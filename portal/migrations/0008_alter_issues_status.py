# Generated by Django 5.0.2 on 2024-02-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_issues_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('answered', 'Answered')], max_length=20),
        ),
    ]

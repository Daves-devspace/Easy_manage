# Generated by Django 5.1.3 on 2024-11-09 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='father_email',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='mother_email',
        ),
    ]

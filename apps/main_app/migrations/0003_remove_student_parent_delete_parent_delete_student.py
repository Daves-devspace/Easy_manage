# Generated by Django 5.1.3 on 2024-11-27 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_parent_father_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.IntegerField(max_length=2),
        ),
    ]

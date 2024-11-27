# Generated by Django 5.1.3 on 2024-11-09 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(max_length=100)),
                ('father_id', models.CharField(max_length=100)),
                ('father_mobile', models.CharField(max_length=100)),
                ('father_email', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(max_length=100)),
                ('mother_id', models.CharField(max_length=100)),
                ('mother_mobile', models.CharField(max_length=100)),
                ('mother_email', models.CharField(max_length=100)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('student_class', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('admission_number', models.CharField(max_length=15)),
                ('section', models.CharField(max_length=15)),
                ('student_image', models.ImageField(blank=True, null=True, upload_to='student/')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.parent')),
            ],
        ),
    ]

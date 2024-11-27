# Generated by Django 5.1.3 on 2024-11-27 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_student_term_fee_alter_student_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('expected_return_date', models.DateField()),
                ('return_date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='students.student')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'transactions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_request_id', models.CharField(max_length=100)),
                ('checkout_request_id', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=30, null=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.transaction')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
                'ordering': ['-created_at'],
            },
        ),
    ]
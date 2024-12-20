# Generated by Django 5.1.3 on 2024-11-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_parent_permanent_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='permanent_address',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='present_address',
        ),
        migrations.AlterField(
            model_name='parent',
            name='father_id',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='parent',
            name='father_mobile',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='parent',
            name='father_occupation',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='parent',
            name='mother_id',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='parent',
            name='mother_mobile',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='parent',
            name='mother_occupation',
            field=models.CharField(max_length=30),
        ),
    ]

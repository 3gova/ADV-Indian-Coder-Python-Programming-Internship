# Generated by Django 4.2.6 on 2023-11-21 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='S_No',
            new_name='sno',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Task_Name',
            new_name='task_name',
        ),
    ]
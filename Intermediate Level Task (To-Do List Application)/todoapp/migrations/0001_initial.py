# Generated by Django 4.2.6 on 2023-11-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('S_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Task_Name', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
    ]

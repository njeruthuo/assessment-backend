# Generated by Django 5.1 on 2024-08-30 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reg', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Yard', 'Yard'), ('Garage', 'Garage')], max_length=10)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asset')),
            ],
        ),
    ]

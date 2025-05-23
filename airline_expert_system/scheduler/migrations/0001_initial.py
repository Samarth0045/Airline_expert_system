# Generated by Django 5.2 on 2025-04-11 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tail_number', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=50)),
                ('max_cargo_weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('weight', models.FloatField()),
                ('priority', models.CharField(choices=[('High', 'High'), ('Normal', 'Normal')], max_length=10)),
                ('flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.flight')),
            ],
        ),
    ]

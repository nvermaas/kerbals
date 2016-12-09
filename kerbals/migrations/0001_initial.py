# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flights', models.IntegerField(default=0)),
                ('land', models.CharField(max_length=255)),
                ('orbit', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kerbal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('trait', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='career',
            name='kerbal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kerbals.Kerbal'),
        ),
    ]
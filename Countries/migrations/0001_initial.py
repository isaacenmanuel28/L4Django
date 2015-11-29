# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=4)),
                ('Country', models.CharField(max_length=4)),
                ('Population', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=4)),
                ('Country', models.CharField(max_length=4)),
            ],
        ),
    ]

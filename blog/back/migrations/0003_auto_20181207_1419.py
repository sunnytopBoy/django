# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_article_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'a_type',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='atype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='back.Atype'),
        ),
    ]

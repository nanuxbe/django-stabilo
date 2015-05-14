# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=50, verbose_name='label')),
                ('slug', models.SlugField(verbose_name='slug')),
            ],
            options={
                'ordering': ('label',),
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=250, verbose_name='keyword')),
                ('category', models.ForeignKey(related_name='keywords', verbose_name='category', to='stabilo.Category')),
            ],
            options={
                'ordering': ('keyword',),
                'verbose_name': 'keyword',
                'verbose_name_plural': 'keywords',
            },
        ),
    ]

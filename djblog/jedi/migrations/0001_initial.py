# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-03 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(blank=True, help_text='Title of slide', max_length=100, verbose_name='Title')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Description')),
                ('link', models.URLField(blank=True, default=None, help_text='Slug of Learn More', null=True, verbose_name='Link')),
                ('video', models.URLField(blank=True, default=None, help_text='Youtube or Vimeo link', null=True, verbose_name='video')),
                ('active', models.BooleanField(default=True, help_text='Slide is active', verbose_name='Active')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]

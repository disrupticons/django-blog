# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(blank=True, to='blog.Comment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(blank=True, to='blog.Post', null=True),
        ),
    ]

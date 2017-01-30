# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('content', models.TextField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'/home/navaneetha/Pictures', blank=True)),
                ('published', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('subscibers', models.IntegerField(default=0)),
                ('subscribe', models.EmailField(max_length=254)),
                ('draft', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('highlighted', models.TextField()),
                ('comment', models.ForeignKey(related_name='comments', to='posts.Comment')),
                ('owner', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['published', 'updated_date'],
            },
        ),
    ]

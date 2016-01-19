# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAgenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

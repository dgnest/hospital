# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalConsultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prescription', models.TextField(verbose_name='prescription')),
                ('diagnosis', models.TextField(verbose_name='diagnosis')),
                ('is_inpatient', models.BooleanField(default=True, verbose_name='is inpatient')),
                ('date_performed', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date performed')),
                ('doctor', models.ForeignKey(verbose_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'medical_consultation',
                'verbose_name': 'medical consultation',
            },
            bases=(models.Model,),
        ),
    ]

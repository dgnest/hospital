# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('dni', models.CharField(max_length=8, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(b'^\\d{8}', 'only valid DNIs are allowed', 'invalid DNI')])),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('age', models.PositiveIntegerField(verbose_name='age', validators=[django.core.validators.MaxValueValidator(150)])),
                ('sex', models.CharField(default=b'M', max_length=1, verbose_name='sex', choices=[(b'M', 'male'), (b'F', 'female'), (b'O', 'other')])),
                ('address', models.CharField(max_length=200, verbose_name='address', blank=True)),
                ('email', models.EmailField(max_length=150, verbose_name='email', blank=True)),
                ('telephone', models.CharField(max_length=15, verbose_name='telephone', blank=True)),
                ('cellphone', models.CharField(max_length=15, verbose_name='cellphone', blank=True)),
                ('is_inpatient', models.BooleanField(default=False, verbose_name='is inpatient')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('superuser', models.ForeignKey(verbose_name='superuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'patient',
                'verbose_name': 'patient',
            },
            bases=(models.Model,),
        ),
    ]

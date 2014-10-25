# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
        ('patient', '0001_initial'),
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalconsultation',
            name='medicines',
            field=models.ManyToManyField(to='medicine.Medicine', verbose_name='medicines', through='medicine.MedicinePerConsultation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalconsultation',
            name='patient',
            field=models.ForeignKey(verbose_name='patient', to='patient.Patient'),
            preserve_default=True,
        ),
    ]

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Medicine(models.Model):
    code = models.CharField(
        max_length=50,
        primary_key=True,
        verbose_name=_('codigo'),
    )
    name = models.CharField(
        max_length=250,
        verbose_name=_('name'),
    )
    description = models.CharField(
        max_length=350,
        blank=True,
        verbose_name=_('description'),
    )
    medicine_type = models.CharField(
        max_length=350,
        blank=True,
        verbose_name=_('medicine type'),
    )
    amount = models.PositiveIntegerField(
        verbose_name=_('amount'),
    )

    def __unicode__(self):
        return unicode(self.code)

    class Meta:
        db_table = 'medicine'
        verbose_name = _('medicine')


class MedicinePerConsultation(models.Model):
    medical_consultation = models.ForeignKey(
        'consultation.MedicalConsultation',
        verbose_name=_('medical consultation'),
    )
    medicine = models.ForeignKey(
        'medicine.Medicine',
        verbose_name=_('medicine'),
    )
    amount = models.PositiveIntegerField(
        verbose_name=_('amount'),
    )

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        db_table = 'medicine_per_consultation'
        verbose_name = _('medicine per consultation')

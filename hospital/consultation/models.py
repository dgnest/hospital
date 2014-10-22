from django.db import models
from django.contrib.auth.models import User
from medicine.models import Medicine
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class MedicalConsultation(models.Model):
    medicines = models.ManyToManyField(
        Medicine,
        through='medicine.MedicinePerConsultation',
        verbose_name=_('medicines'),
    )
    doctor = models.ForeignKey(
        User,
        verbose_name=_('doctor'),
    )
    patient = models.ForeignKey(
        'patient.Patient',
        verbose_name=_('patient'),
    )
    prescription = models.TextField(
        verbose_name=_('prescription'),
    )
    diagnosis = models.TextField(
        verbose_name=_('diagnosis'),
    )
    is_inpatient = models.BooleanField(
        default=True,
        verbose_name=_('is inpatient'),
    )
    date_performed = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('date performed'),
    )

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        db_table = 'medical_consultation'
        verbose_name = _('medical consultation')

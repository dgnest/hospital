from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, RegexValidator
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):
    dni = models.CharField(
        max_length=8,
        primary_key=True,
        validators=[
            RegexValidator(
                r'^\d{8}',
                _('only valid DNIs are allowed'),
                _('invalid DNI'),
            ),
        ],
    )
    superuser = models.ForeignKey(
        User,
        verbose_name=_('superuser'),
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=_('first name'),
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_('last name'),
    )
    age = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(150),
        ],
        verbose_name=_('age'),
    )

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    SEX = (
        (MALE, _('male')),
        (FEMALE, _('female')),
        (OTHER, _('other')),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=MALE,
        verbose_name=_('sex'),
    )
    address = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_('address'),
    )
    email = models.EmailField(
        max_length=150,
        blank=True,
        verbose_name=_('email'),
    )
    telephone = models.CharField(
        max_length=15,
        blank=True,
        verbose_name=_('telephone'),
    )
    cellphone = models.CharField(
        max_length=15,
        blank=True,
        verbose_name=_('cellphone'),
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('date joined'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is active'),
    )

    def __unicode__(self):
        return unicode(self.dni)

    class Meta:
        db_table = 'patient'
        verbose_name = _('patient')

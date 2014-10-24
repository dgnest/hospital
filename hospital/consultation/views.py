from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import permissions
from hospital.permissions import IsSuperuserOrReadOnly
from hospital.mixins import LoginRequiredMixin
from .serializers import MedicalConsultationSerializer
from .models import MedicalConsultation
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _


class MedicalConsultationViewSet(viewsets.ModelViewSet):

    queryset = MedicalConsultation.objects.all()
    serializer_class = MedicalConsultationSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperuserOrReadOnly,
    )
    filter_fields = (
        'doctor',
        'patient',
        'is_inpatient',
    )

    def pre_save(self, obj):
        user = self.request.user
        obj.doctor = user
        super(MedicalConsultationViewSet, self).pre_save(obj)

from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import permissions
from hospital.permissions import IsSuperuserOrReadOnly
from hospital.mixins import LoginRequiredMixin
from .serializers import MedicalConsultationSerializer
from .models import MedicalConsultation
from patient.models import Patient
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


def medical_consultation(request, dni):
    if not request.user.is_authenticated():
        return HttpResponseNotAllowed(['GET'])

    patient = Patient.objects.get(pk=dni)
    ctx = {'patient': patient}

    return render_to_response(
        'consultation/create.html',
        ctx,
        context_instance=RequestContext(request),
    )


def medical_history(request, dni):
    if not request.user.is_authenticated():
        return HttpResponseNotAllowed(['GET'])

    consultations = MedicalConsultation.objects.filter(patient=dni)
    ctx = {'consultations': consultations}

    return render_to_response(
        'consultation/list.html',
        ctx,
        context_instance=RequestContext(request),
    )


def detailed_consultation(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseNotAllowed(['GET'])

    consultation = get_object_or_404(MedicalConsultation, pk=pk)
    ctx = {'consultation': consultation}

    return render_to_response(
        'consultation/detail.html',
        ctx,
        context_instance=RequestContext(request),
    )

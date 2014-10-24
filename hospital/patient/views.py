from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import permissions
from hospital.permissions import IsSuperuserOrReadOnly
from hospital.mixins import LoginRequiredMixin
from .serializers import PatientSerializer
from .models import Patient
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _


class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperuserOrReadOnly,
    )
    filter_fields = (
        'superuser',
        'first_name',
        'last_name',
        'sex',
        'email',
        'telephone',
        'cellphone',
        'is_inpatient',
    )

    def pre_save(self, obj):
        user = self.request.user
        obj.superuser = user
        super(PatientViewSet, self).pre_save(obj)


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patient/list.html'


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient/detail.html'


# solo como superuser
class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_app:patients-list')
    template_name = 'patient/delete.html'


def record_patient(request):
    dni = request.POST['dni']
    superuser = request.user
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    sex = request.POST['sex']
    address = request.POST['address']
    email = request.POST['email']
    telephone = request.POST['telephone']
    cellphone = request.POST['cellphone']
    is_inpatient = request.POST.get('is_inpatient', False)

    patient = Patient.objects.create(
        dni=dni,
        superuser=superuser,
        first_name=first_name,
        last_name=last_name,
        age=age,
        sex=sex,
        address=address,
        email=email,
        telephone=telephone,
        cellphone=cellphone,
        is_inpatient=is_inpatient,
    )

    return patient


def patient_create_view(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            patient = record_patient(request)
            if patient:
                return HttpResponseRedirect(
                    reverse('patient_app:patients-list')
                )

        return render_to_response(
            'patient/create.html',
            context_instance=RequestContext(request),
        )

    return HttpResponseNotAllowed(['GET'])


def update_patient(request, dni):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    sex = request.POST['sex']
    address = request.POST['address']
    email = request.POST['email']
    telephone = request.POST['telephone']
    cellphone = request.POST['cellphone']
    is_inpatient = request.POST.get('is_inpatient', False)

    patient = get_object_or_404(Patient, pk=dni)
    patient.first_name = first_name
    patient.last_name = last_name
    patient.age = age
    patient.sex = sex
    patient.address = address
    patient.email = email
    patient.telephone = telephone
    patient.cellphone = cellphone
    patient.is_inpatient = is_inpatient
    patient.save()

    return patient


def patient_update_view(request, dni):
    if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            patient = update_patient(request, dni)
            if patient:
                return HttpResponseRedirect(
                    reverse('patient_app:patients-list')
                )

        patient = get_object_or_404(Patient, pk=dni)

        ctx = {'patient': patient}

        return render_to_response(
            'patient/update.html',
            ctx,
            context_instance=RequestContext(request),
        )

    return HttpResponseNotAllowed(['GET'])

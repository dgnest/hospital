from rest_framework import viewsets
from rest_framework import permissions
from patient.permissions import IsSuperuserOrReadOnly
from .serializers import PatientSerializer
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils.translation import ugettext_lazy as _


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


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

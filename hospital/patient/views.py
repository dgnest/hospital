from rest_framework import viewsets
from rest_framework import permissions
from patient.permissions import IsSuperuserOrReadOnly
from .serializers import PatientSerializer
from .models import Patient
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
    )

    def pre_save(self, obj):
        user = self.request.user
        obj.superuser = user
        super(PatientViewSet, self).pre_save(obj)

from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import permissions
from hospital.permissions import IsSuperuserOrReadOnly
from hospital.mixins import LoginRequiredMixin
from .serializers import MedicineSerializer
from .models import Medicine
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _


class MedicineViewSet(viewsets.ModelViewSet):

    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperuserOrReadOnly,
    )
    filter_fields = (
        'name',
        'medicine_type',
    )


class MedicineListView(LoginRequiredMixin, ListView):
    model = Medicine
    template_name = 'medicine/list.html'


class MedicineDetailView(LoginRequiredMixin, DetailView):
    model = Medicine
    pk_url_kwarg = 'code'
    template_name = 'medicine/detail.html'


# solo como superuser
class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine
    success_url = reverse_lazy('medicine_app:medicines-list')
    pk_url_kwarg = 'code'
    template_name = 'medicine/delete.html'


def record_medicine(request):
    code = request.POST['code']
    name = request.POST['name']
    description = request.POST['description']
    medicine_type = request.POST['medicine_type']
    amount = request.POST['amount']

    medicine = Medicine.objects.create(
        code=code,
        name=name,
        description=description,
        medicine_type=medicine_type,
        amount=amount,
    )

    return medicine


def medicine_create_view(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            medicine = record_medicine(request)
            if medicine:
                return HttpResponseRedirect(
                    reverse('medicine_app:medicines-list')
                )

        return render_to_response(
            'medicine/create.html',
            context_instance=RequestContext(request),
        )

    return HttpResponseNotAllowed(['GET'])


def update_medicine(request, code):
    name = request.POST['name']
    description = request.POST['description']
    medicine_type = request.POST['medicine_type']
    amount = request.POST['amount']

    medicine = get_object_or_404(Medicine, pk=code)
    medicine.name = name
    medicine.description = description
    medicine.medicine_type = medicine_type
    medicine.amount = amount
    medicine.save()

    return medicine


def medicine_update_view(request, code):
    if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            medicine = update_medicine(request, code)
            if medicine:
                return HttpResponseRedirect(
                    reverse('medicine_app:medicines-list')
                )

        medicine = get_object_or_404(Medicine, pk=code)

        ctx = {'medicine': medicine}

        return render_to_response(
            'medicine/update.html',
            ctx,
            context_instance=RequestContext(request),
        )

    return HttpResponseNotAllowed(['GET'])

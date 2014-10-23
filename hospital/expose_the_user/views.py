from django.shortcuts import render_to_response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from hospital.permissions import IsSuperuserOrReadOnly
from hospital.mixins import LoginRequiredMixin
from .serializers import UserSerializer
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperuserOrReadOnly,
    )
    filter_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_superuser',
    )

    def pre_save(self, obj):
        obj.set_password(obj.password)
        super(UserViewSet, self).pre_save(obj)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'expose_the_user/list.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'expose_the_user/detail.html'


# solo como superuser
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user_app:users-list')
    template_name = 'expose_the_user/delete.html'


def record_user(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    is_superuser = request.POST.get('is_superuser', False)

    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_superuser=is_superuser,
    )

    return user


def user_create_view(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            user = record_user(request)
            if user:
                return HttpResponseRedirect(
                    reverse('user_app:users-list')
                )

        return render_to_response(
            'expose_the_user/create.html',
            context_instance=RequestContext(request),
        )

    return HttpResponseNotAllowed(['GET'])


def update_user(request, pk):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    is_superuser = request.POST.get('is_superuser', False)

    user = get_object_or_404(User, pk=pk)
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.is_superuser = is_superuser
    user.save()

    return user


def user_update_view(request, pk):
    if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            user = update_user(request, pk)
            if user:
                return HttpResponseRedirect(
                    reverse('user_app:users-list')
                )

        user = get_object_or_404(User, pk=pk)

        ctx = {'my_user': user}

        return render_to_response(
            'expose_the_user/update.html',
            ctx,
            context_instance=RequestContext(request),
        )

    return HttpResponseNotAllowed(['GET'])

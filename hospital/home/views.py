from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('patient_app:patients-list'))

    message = ""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(
                    reverse('patient_app:patients-list')
                )
        else:
            message = _("Incorrect username or password")

    ctx = {
        'message': message,
    }
    return render_to_response(
        'home/login.html',
        ctx,
        context_instance=RequestContext(request),
    )


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home_app:login'))

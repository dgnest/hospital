from django.conf.urls import patterns, url
from .views import patient_list_view, PatientDetailView, PatientDeleteView
from .views import patient_create_view, patient_update_view


urlpatterns = patterns(
    '',
    url(r'^$', patient_list_view, name='patients-list'),
    url(
        r'^create/$',
        patient_create_view,
        name='patients-create',
    ),
    url(
        r'^delete/(?P<pk>[\w]+)/$',
        PatientDeleteView.as_view(),
        name='patients-delete',
    ),
    url(
        r'^update/(?P<dni>[\w]+)/$',
        patient_update_view,
        name='patients-update',
    ),
    url(
        r'^(?P<pk>[\w]+)/$',
        PatientDetailView.as_view(),
        name='patients-detail',
    ),
)

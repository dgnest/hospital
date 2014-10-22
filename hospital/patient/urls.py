from django.conf.urls import patterns, url
from .views import PatientListView, PatientDetailView


urlpatterns = patterns(
    '',
    url(r'^patients/$', PatientListView.as_view(), name='patients-list'),
    url(
        r'^patients/(?P<pk>[\w]+)/$',
        PatientDetailView.as_view(), 
        name='patients-detail',
    ),
)

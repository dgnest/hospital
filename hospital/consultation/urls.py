from django.conf.urls import patterns, url
from .views import medical_consultation, medical_history
from .views import detailed_consultation


urlpatterns = patterns(
    '',
    url(
        r'^(?P<dni>[\w]+)/$',
        medical_consultation,
        name='medical-consultation',
    ),
    url(
        r'^history/(?P<dni>[\w]+)/$',
        medical_history,
        name='medical-history',
    ),
    url(
        r'^detail/(?P<pk>[\w]+)/$',
        detailed_consultation,
        name='detailed-consultation',
    ),
)

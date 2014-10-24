from django.conf.urls import patterns, url
from .views import MedicineListView, MedicineDetailView, MedicineDeleteView
from .views import medicine_create_view, medicine_update_view


urlpatterns = patterns(
    '',
    url(r'^$', MedicineListView.as_view(), name='medicines-list'),
    url(
        r'^create/$',
        medicine_create_view,
        name='medicines-create',
    ),
    url(
        r'^delete/(?P<code>[\w]+)/$',
        MedicineDeleteView.as_view(),
        name='medicines-delete',
    ),
    url(
        r'^update/(?P<code>[\w]+)/$',
        medicine_update_view,
        name='medicines-update',
    ),
    url(
        r'^(?P<code>[\w]+)/$',
        MedicineDetailView.as_view(),
        name='medicines-detail',
    ),
)

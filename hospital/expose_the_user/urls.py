# from django.conf.urls import patterns, url
# from .views import PatientListView, PatientDetailView, PatientDeleteView
# from .views import patient_create_view, patient_update_view


# urlpatterns = patterns(
#     '',
#     url(r'^patients/$', PatientListView.as_view(), name='patients-list'),
#     url(
#         r'^patients/create/$',
#         patient_create_view,
#         name='patients-create',
#     ),
#     url(
#         r'^patients/delete/(?P<pk>[\w]+)/$',
#         PatientDeleteView.as_view(),
#         name='patients-delete',
#     ),
#     url(
#         r'^patients/update/(?P<dni>[\w]+)/$',
#         patient_update_view,
#         name='patients-update',
#     ),
#     url(
#         r'^patients/(?P<pk>[\w]+)/$',
#         PatientDetailView.as_view(),
#         name='patients-detail',
#     ),
# )

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from patient.views import PatientViewSet
from expose_the_user.views import UserViewSet
from medicine.views import MedicineViewSet, MedicinePerConsultationViewSet
from consultation.views import MedicalConsultationViewSet


router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'users', UserViewSet)
router.register(r'medicines', MedicineViewSet)
router.register(r'medicines-per-consultation', MedicinePerConsultationViewSet)
router.register(r'consultations', MedicalConsultationViewSet)


urlpatterns = patterns(
    '',
    # Grappelli urls.
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Browsable API.
    url(r'^api/', include(router.urls)),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    # Home app.
    url(r'^', include('home.urls', namespace='home_app')),
    # Patient app.
    url(r'^patients/', include('patient.urls', namespace='patient_app')),
    # User app.
    url(r'^users/', include('expose_the_user.urls', namespace='user_app')),
    # Medicine app.
    url(r'^medicines/', include('medicine.urls', namespace='medicine_app')),
    # Medicine app.
    url(r'^consultation/', include('consultation.urls', namespace='consultation_app')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    )

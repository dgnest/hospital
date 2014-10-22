from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from patient.views import PatientViewSet


router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)


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
    url(r'^', include('patient.urls', namespace='patient_app')),
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

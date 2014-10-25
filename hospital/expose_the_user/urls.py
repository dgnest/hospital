from django.conf.urls import patterns, url
from .views import user_list_view, UserDetailView, UserDeleteView
from .views import user_create_view, user_update_view


urlpatterns = patterns(
    '',
    url(r'^$', user_list_view, name='users-list'),
    url(
        r'^create/$',
        user_create_view,
        name='users-create',
    ),
    url(
        r'^delete/(?P<pk>[\w]+)/$',
        UserDeleteView.as_view(),
        name='users-delete',
    ),
    url(
        r'^update/(?P<pk>[\w]+)/$',
        user_update_view,
        name='users-update',
    ),
    url(
        r'^(?P<pk>[\w]+)/$',
        UserDetailView.as_view(),
        name='users-detail',
    ),
)

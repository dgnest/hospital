from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from hospital.permissions import IsSuperuserOrReadOnly
from .serializers import UserSerializer


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

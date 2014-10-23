from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):

    """
    Custom permission to only allow superusers to edit.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            return request.user.is_superuser
        except AttributeError:
            return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

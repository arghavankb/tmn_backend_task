from rest_framework import permissions


# Defining custom permission for ProductViewSet and ProductImageViewSet
class AdminModifyAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

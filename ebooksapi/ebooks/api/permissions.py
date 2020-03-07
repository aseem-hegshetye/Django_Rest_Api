from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return is_admin or request.method in permissions.SAFE_METHODS


class ReviewAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.review_author or request.method in permissions.SAFE_METHODS:
            return True
        return False

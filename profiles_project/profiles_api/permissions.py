from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """ CHeck user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ allow user can only update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.user_profile.id

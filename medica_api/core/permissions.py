from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    """
        user can see or update only their own profile
    """

    def has_object_permission(self, request, view, obj):
        """ we have already disabled List method. so get method here will come with id"""
        print(f'request.method ={request.method }')
        print(f'request.user.id = {request.user.id}, obj.id={obj.id}')
        if request.method in ['PUT', 'PATCH', 'GET']:
            return request.user.id == obj.id
        else:
            return True

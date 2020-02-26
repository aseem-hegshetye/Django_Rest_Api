from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import models
from . import permissions
from .serializers import *


class HelloAPIView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        api_list = [
            'item1',
            'item2'

        ]
        return Response({'message': 'test view', 'data': api_list}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """create hello message with our name """

        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, response, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, response, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, response, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ test api view set"""
    serializer_class = HelloSerializer  # keep serializer class here at top so that django will show this in browsers API view

    def list(self, request):
        api_viewset = [
            'asidas',
            'aosidjais'
        ]
        return Response({'message': api_viewset}, status=status.HTTP_200_OK)

    def create(self, request):
        """ create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'get'})

    def update(self, request, pk=None):
        return Response({'method': 'put'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'patch'})

    def destroy(self, request, pk=None):
        return Response({'method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
        handle creating and updating profile
        authentication -

    """
    serializer_class = UserProfileSerializer
    queryset = models.CustomUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'email')


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# token: 3b582ecfa00f0363ad7d306f006d0af2bf84ddc4

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ handle profile feed updates and creation"""
    queryset = models.ProfileFeedItem.objects.all()
    serializer_class = ProfileFeedSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """ overwritting POST request made to create new object"""
        serializer.save(user_profile=self.request.user)

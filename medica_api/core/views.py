from django.shortcuts import render
from . import models
from rest_framework import viewsets
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomUserPermission
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class User(mixins.CreateModelMixin,
           mixins.RetrieveModelMixin,
           mixins.UpdateModelMixin,
           mixins.DestroyModelMixin,
           GenericViewSet):
    """
        Api for customuser model
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        CustomUserPermission,
    )

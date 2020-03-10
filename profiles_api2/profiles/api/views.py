from rest_framework import generics
from ..models import Profile,ProfileStatus
from .serializers import ProfileSerializer, ProfileStatusSerializer
from rest_framework import permissions
from rest_framework import viewsets, mixins
from . import permissions as custom_perm
from rest_framework.viewsets import ModelViewSet


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [custom_perm.IsOwnProfileOrReadOnly]


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [custom_perm.IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.user_profile
        serializer.save(user_profile = user_profile)
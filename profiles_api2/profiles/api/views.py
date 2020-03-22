from rest_framework import generics
from ..models import Profile, ProfileStatus
from .serializers import ProfileSerializer, ProfileStatusSerializer, \
    ProfileAvatarSerializer
from rest_framework import permissions
from rest_framework import viewsets, mixins
from . import permissions as custom_perm
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    __basic_fields = ('city', 'bio')
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [custom_perm.IsOwnProfileOrReadOnly]

    # filters
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = __basic_fields
    search_fields = __basic_fields


class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [custom_perm.IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class AvatarViewSet(mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileAvatarSerializer

    permission_classes = [custom_perm.AvatarPermissions]
    #
    # def get_object(self):
    #     return self.request.user.profile

from django.urls import path, include
from .api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles2',ProfileViewSet,basename='profiles2')
router.register('profiles2status',ProfileStatusViewSet,basename='status')
router.register('avatar',AvatarViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
]

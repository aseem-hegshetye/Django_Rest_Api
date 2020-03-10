from django.urls import path, include
from .api.views import ProfileList,ProfileViewSet,ProfileStatusViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles2',ProfileViewSet)
router.register('profiles2status',ProfileStatusViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
]

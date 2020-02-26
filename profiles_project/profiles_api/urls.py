from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile',UserProfileViewSet,basename='user-viewset')
router.register('feed',UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view()),
    path('login/',UserLoginApiView.as_view()),
    path('', include(router.urls))
]

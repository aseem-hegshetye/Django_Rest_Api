from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register('user', User, basename='user')

urlpatterns = [
    path('', include(router.urls))
]

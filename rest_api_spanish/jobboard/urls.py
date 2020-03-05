from django.urls import path, include
from .api.views import *

urlpatterns = [
    path('', JobBoardList.as_view(), name='jobboard-list'),
    path('<int:pk>/', JobBoardDetails.as_view(), name='jobboard-details'),
]

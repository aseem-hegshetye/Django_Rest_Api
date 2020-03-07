from django.urls import include, path
from .api.views import *

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', EbookDetailAPIView.as_view(), name='ebook-detail'),  # default lookup_field is pk

    path('ebook/<int:ebook_pk>/review/', ReviewCreateAPIView.as_view(), name='ebook-review'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),  # default lookup_field is pk
]

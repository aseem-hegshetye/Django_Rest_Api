from django.urls import path, include
from quotesapi.api.views import QuotesListCreateAPIView,QuoteDetailView

urlpatterns = [
    path('quotes/', QuotesListCreateAPIView.as_view(), name='quotes-list'),
    path('quotes/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
]

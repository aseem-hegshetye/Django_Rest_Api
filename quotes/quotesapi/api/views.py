from rest_framework import generics
from ..models import Quote
from .serializer import QuoteSerializer
from .permissions import IsAdminOrReadOnly


class QuotesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]
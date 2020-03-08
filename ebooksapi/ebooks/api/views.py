from rest_framework import generics
from rest_framework import mixins
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from . import permissions as custom_permission
from rest_framework.exceptions import ValidationError
from . import pagination


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")  # negative id = order by id desc
    serializer_class = EbookSerializer
    permission_classes = [custom_permission.IsAdminOrReadOnly]
    pagination_class = pagination.SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        review_author = self.request.user
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        queryset2 = Review.objects.filter(pk=ebook_pk, review_author=review_author)
        if queryset2.exists():
            raise ValidationError('You already have a review for this book')
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [custom_permission.ReviewAuthorOrReadOnly]

# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

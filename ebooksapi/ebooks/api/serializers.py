from rest_framework import serializers
from ..models import *


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('ebook',)


class EbookSerializer(serializers.ModelSerializer):
    # add extra field to show all reviews per ebook.
    # related_name is reviews in models.py hence using this variable name here
    reviews = ReviewSerializer(many=True,
                               read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'

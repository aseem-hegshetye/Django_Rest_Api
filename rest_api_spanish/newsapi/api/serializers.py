from rest_framework import serializers
from newsapi.models import *
from datetime import datetime
from django.utils.timesince import timesince


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField(min_length=10)
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateField(read_only=True)
#     updated_at = serializers.DateField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, attrs):
#         """
#         Overwritting validate func.
#         :param attrs: data from serializer.
#         :return: validated data
#         """
#         if attrs['title'] == attrs['description']:
#             # raise exception which will be caught by func run_validation
#             raise serializers.ValidationError("Title and desc must be different")
#         return attrs
#
#     def validate_author(self, value):
#         """
#         validation for field = author.
#         :param value: value of field author
#         """
#         if value.lower() == 'aseem':
#             raise serializers.ValidationError("Aseem you are great. we cant save u")
#         return value


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()  # new field

    # author_name = serializers.SerializerMethodField()

    # author=serializers.StringRelatedField()
    # author= JournalistSerializer(read_only=True)

    class Meta:
        model = Article
        # fields="__all__" # all fields
        # fields = ('id','author','title')  # certain fields
        exclude = ('updated_at',)  # exclude certain fields

    def get_time_since_publication(self, object):
        """
        :return: value for field time_since_publication
        """
        time_delta = timesince(object.publication_date, now=datetime.now())
        return time_delta

    def get_author_name(self, object):
        author_name = object.author.first_name
        return author_name

    def validate(self, attrs):
        """
        Overwritting validate func.
        :param attrs: data from serializer.
        :return: validated data
        """
        if attrs['title'] == attrs['description']:
            # raise exception which will be caught by func run_validation
            raise serializers.ValidationError("Title and desc must be different")
        return attrs

    def validate_author(self, value):
        """
        validation for field = author.
        :param value: value of field author
        """
        if value.lower() == 'aseem':
            raise serializers.ValidationError("Aseem you are great. we cant save u")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    # related_name = articles in models.py, hence we use 'articles' below
    # articles = ArticleSerializer(many=True, read_only=True)

    articles = serializers.HyperlinkedRelatedField(
        view_name='get_article_detail_apiview',
        read_only=True,
        many=True
    )

    class Meta:
        model = Journalist
        fields = "__all__"

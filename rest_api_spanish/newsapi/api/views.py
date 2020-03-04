from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from newsapi.models import Article
from newsapi.api.serializers import ArticleSerializer


@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    if request.method == 'GET':
        article = Article.objects.filter(active=True)
        serializer = ArticleSerializer(article, many=True)
        data = serializer.data

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        else:
            data = serializer.errors

    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def article_detail_create_api_view(request, pk):
    article = Article.objects.get(active=True, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = ArticleSerializer(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListApiView(APIView):
    def get(self, request):
        article = Article.objects.filter(active=True)
        serializer = ArticleSerializer(article, many=True)
        data = serializer.data
        return Response(data=data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        else:
            data = serializer.errors
        return Response(data=data)


class ArticleDetailApiView(APIView):

    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

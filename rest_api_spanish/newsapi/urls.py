from django.urls import path, include
from .api.views import article_list_create_api_view, article_detail_create_api_view
from .api.views import ArticleDetailApiView, ArticleListApiView
from .api.views import JournalistListCreateApiView

urlpatterns = [
    path('articles/', article_list_create_api_view, name='get_articles'),
    path('articles/<int:pk>/', article_detail_create_api_view, name='get_article_detail'),

    path('articles_apiview/', ArticleListApiView.as_view(), name='get_articles_apiview'),
    path('articles_apiview/<int:pk>/', ArticleDetailApiView.as_view(), name='get_article_detail_apiview'),

    path('journalist_apiview/',JournalistListCreateApiView.as_view(),name='jounalist-list'),
]

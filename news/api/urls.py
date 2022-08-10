from django.urls import path

from news.api.views import ArticleListCreateAPIView, ArticleDetailAPIView
# article_list_create_api_view, article_detail_api_view,

urlpatterns = [
    # path("articles/", view=article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", view=article_detail_api_view, name="article-detail"),
    path("articles/", view=ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", view=ArticleDetailAPIView.as_view(),
         name="article-detail"),
]

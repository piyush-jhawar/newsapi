from multiprocessing import context
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer
from drf_spectacular.utils import extend_schema


class ArticleListCreateAPIView(APIView):

    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @extend_schema(request=ArticleSerializer, responses=None)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @extend_schema(request=ArticleSerializer, responses=None) 
    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(request=ArticleSerializer, responses=None)
    def patch(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListCreateAPIView(APIView):

    @extend_schema(request=None, responses=JournalistSerializer)
    def get(self, request):
        journalist = Journalist.objects.all()
        serializer = JournalistSerializer(journalist, many=True, context={'request' : request})
        return Response(serializer.data)

    @extend_schema(request=JournalistSerializer, responses=None)
    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalistDetailAPIView(APIView):

    def get_object(self, pk):
        journalist = get_object_or_404(Journalist, pk=pk)
        return journalist

    def get(self, request, pk):
        journalist = self.get_object(pk=pk)
        serializer = JournalistSerializer(journalist)
        return Response(serializer.data)

    @extend_schema(request=JournalistSerializer, responses=None) 
    def put(self, request, pk):
        journalist = self.get_object(pk=pk)
        serializer = JournalistSerializer(journalist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(request=JournalistSerializer, responses=None)
    def patch(self, request, pk):
        journalist = self.get_object(pk=pk)
        serializer = JournalistSerializer(journalist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        journalist = self.get_object(pk=pk)
        journalist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# @api_view(["GET", "POST"])
# def article_list_create_api_view(request):
#     if request.method == "GET":
#         articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def article_detail_api_view(request, pk):

#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return Response({"error": {
#             "code": 404,
#             "message": "Article not found"}}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "PATCH":
#         serializer = ArticleSerializer(
#             article, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

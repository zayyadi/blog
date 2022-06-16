from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Category, Article, Comment
from blog_api.serializer import CategorySerializer, ArticleSerializer, CommentSerializer 

# Create your views here.
class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ArticleList(APIView):
    """
    Return list of all articles
    """

    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

class ArticleByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Article.objects.filter(category__slug=query)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
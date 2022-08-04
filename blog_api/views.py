from django.shortcuts import render, get_object_or_404

from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from blog.models import Category, Article, Comment
from blog_api.serializer import CategorySerializer, ArticleSerializer, CommentSerializer

from knox.auth import TokenAuthentication

# Create your views here.
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListDetailfilter(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


class ArticleByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Article.objects.filter(category__slug=query)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


class ArticleDetailView(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes =[permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=item)

class CreateArticle(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes =[permissions.IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]

    def get(self):
        return self.request.user

    def post(self, request, format=None):
        print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EditArticle(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer

class DeleteArticle(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer

class CommentView(APIView):

    def get(self, request, query=None):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


from rest_framework import serializers
from blog.models import Article, Comment, Category

from taggit.serializers import (
    TagListSerializerField,
    TaggitSerializer
)

class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    tags = TagListSerializerField()
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'author',
            'content',
            'image',
            'publish',
            'tags',
            'category',
            'likes',
            'snippet',
        )
    def get_image(self, obj):
        return obj.image.url

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'name',
            'body',
            'publish',
            'active',
            'parent',
        )

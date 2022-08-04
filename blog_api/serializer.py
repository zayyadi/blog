from rest_framework import serializers
from blog.models import Article, Comment, Category

from django.contrib.auth import authenticate

from taggit.serializers import (
    TagListSerializerField,
    TaggitSerializer
)

from django.contrib.auth.models import User

class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    tags = TagListSerializerField()
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'slug',
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


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


# class UserRegisterSerializer(serializers.ModelSerializer):

#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(min_length=8, write_only=True)

#     class Meta:
#         model = User
#         fields = ('email', 'username', 'first_name')
#         extra_kwargs = {'password': {'write_only': True}}
from rest_framework import serializers
from .models import Category, Idea, UserProfile
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class IdeaSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = serializers.StringRelatedField()  # Displays author's username
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Idea
        fields = ['id', 'title', 'content', 'category', 'author', 'created_at', 'likes', 'likes_count']
        read_only_fields = ['author', 'created_at', 'likes']

    def get_likes_count(self, obj):
        return obj.likes.count()

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    saved_ideas = IdeaSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'saved_ideas', 'streak']
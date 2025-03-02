from rest_framework import serializers
from .models import Category, Idea, UserProfile
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class IdeaSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = serializers.StringRelatedField()  # Displays author's username
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Idea
        fields = ['id', 'title', 'content', 'category', 'author', 'created_at', 'likes_count']
        read_only_fields = ['id', 'author', 'created_at', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Idea.objects.create(author=user, **validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    saved_ideas = IdeaSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'saved_ideas', 'streak']
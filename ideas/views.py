from django.shortcuts import render, redirect

# Create your views here.
from .models import Idea, Category
from .serializers import IdeaSerializer, CategorySerializer, UserProfileSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    ideas = Idea.objects.all().order_by('-created_at')[:10]  # Latest 10 ideas
    categories = Category.objects.all()
    return render(request, 'ideas/home.html', {'ideas': ideas, 'categories': categories})

def idea_detail(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})


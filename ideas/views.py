from django.shortcuts import render, redirect

# Create your views here.
from .models import Idea, Category
from .serializers import IdeaSerializer, CategorySerializer, UserProfileSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import IdeaForm, CategoryForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    ideas = Idea.objects.all().order_by('-created_at')[:10]  # Latest 10 ideas
    categories = Category.objects.all()
    return render(request, 'ideas/home.html', {'ideas': ideas, 'categories': categories})

def idea_detail(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

def create_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user  # Set the current logged-in user as the author
            idea.save()
            return redirect('home')  # Redirect to the home page or idea list
    else:
        form = IdeaForm()
    return render(request, 'ideas/create_idea.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or category list
    else:
        form = CategoryForm()
    return render(request, 'ideas/create_category.html', {'form': form})
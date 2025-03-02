from django import forms
from .models import Idea, Category

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'content', 'category']  # Add 'category' if you want to assign categories to ideas

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
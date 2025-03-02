from django.contrib import admin

# Register your models here.
from .models import Category, Idea, UserProfile

admin.site.register(Category)
admin.site.register(Idea)
admin.site.register(UserProfile)
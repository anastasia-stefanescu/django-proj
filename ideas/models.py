from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # The bite-sized knowledge
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_ideas', blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_ideas = models.ManyToManyField(Idea, blank=True)
    streak = models.IntegerField(default=0)  # For gamification

    def __str__(self):
        return self.user.username

# Create your models here.

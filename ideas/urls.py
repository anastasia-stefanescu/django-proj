from django.urls import path
from .views import home, idea_detail

urlpatterns = [
    path('', home, name='home'),
    path('idea/<int:idea_id>/', idea_detail, name='idea_detail'),
]
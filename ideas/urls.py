from django.urls import path
from .views import home, idea_detail, create_category, create_idea
from .api_views import api_overview, idea_list_create, idea_detail

urlpatterns = [
    path('', home, name='home'),
    #path('idea/<int:idea_id>/', idea_detail, name='idea_detail'),
    path('api/', api_overview, name='api_overview'),
    path('api/ideas/', idea_list_create, name='idea_list_create'),
    path('api/ideas/<int:idea_id>/', idea_detail, name='idea_detail'),
    path('create-idea/', create_idea, name='create_idea'),
    path('create-category/', create_category, name='create_category'),
]
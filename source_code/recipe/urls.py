"""ITW2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import RecipeListView, RecipeDeleteView, UserRecipeListView, RecipeDetailView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-home'),
    path('contact/', views.contact, name='recipe-contact'),
    path('about/', views.about, name='recipe-about'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('category/<cat_name>/', views.category, name='recipe-category'),
    path('type/<typ_name>/', views.type, name='recipe-type'),
    path('recipe/new/', views.RecipeCreateView, name='recipe-create'),
    path('recipe/<pk>/update/', views.RecipeUpdateView, name='recipe-update'),
    path('recipe/<pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),    
    path('recipe/<str:usr_name>/', UserRecipeListView.as_view(), name='user-recipe'),

]
#path('recipe/<pk>/', RecipeDetailView.as_view(), name='single-recipe'),
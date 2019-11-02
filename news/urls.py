from django.urls import path
from . import views
from .views import (
	ArticlesListView, 
	ArticleDetailView, 
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView,
	UserArticlesListView,
)
from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
	path('', ArticlesListView.as_view(), name="news"),
	path('user/<str:username>', UserArticlesListView.as_view(), name="user-posts"),
	path('<int:pk>/', ArticleDetailView.as_view(), name="post-detail"),
	path('<int:pk>/update/', ArticleUpdateView.as_view(), name="post-update"),
	path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="post-delete"),
	path('create/', ArticleCreateView.as_view(), name="post-create")
]
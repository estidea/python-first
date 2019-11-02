from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Articles
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
)


class ArticlesListView(ListView):
	model = Articles
	template_name = 'news/posts.html'
	context_object_name = 'articles'
	ordering = ['-date']
	paginate_by = 5

class UserArticlesListView(ListView):
	model = Articles
	template_name = 'news/user_posts.html'
	context_object_name = 'articles'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Articles.objects.filter(author=user).order_by('-date')


class ArticleDetailView(DetailView):
	model = Articles
	template_name = 'news/post.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Articles
	fields = ['title', 'text']
	template_name = 'news/post_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Articles
	fields = ['title', 'text']
	template_name = 'news/post_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Articles
	template_name = 'news/post_confirm_delete.html'
	success_url = '/news'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
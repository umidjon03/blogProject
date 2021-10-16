from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class BlogPostView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogPostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ['title', 'summary', 'author', 'body']


class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'summary', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'deleter.html'
    success_url = reverse_lazy('main')
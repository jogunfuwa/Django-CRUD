from django.shortcuts import render


# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.edit import ListView, CreateView, DetailView, UpdateView, DeleteView


class PostListView(generic.ListView):
    model= Post
    template_name= "blog/post-list.html"

class PostCreateView(generic.CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
   
    template_name= "blog/post-form.html"
   
class PostDetailView(generic.DetailView):
    method= Post
    template_name= "blog/post-detail.html"

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
    template_name= "blog/post-form.html"

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
    template_name= "blog/post-confirm-delete.html"

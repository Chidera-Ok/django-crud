from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.
class BlogCreateView(CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class BlogListView(ListView):
    model = Post

class BlogDetailView(DetailView):
    model = Post

class BlogUpdateView(UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
class BlogDeleteView(DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

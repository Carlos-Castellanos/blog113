# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import( 
    CreateView, 
    DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
   )   #113

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# https://docs.djangoproject.com/en/4.1/ref/class-based-views/flattened-index/
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class PostListView(ListView):
    template_name = "posts/list.html"   
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"  
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #113
    template_name = "posts/new.html"  
    model = Post
    fields = ["title","subtitle","body", "image"]  

    def form_valid(self, form):       #take tha user and save it like author'field
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #113
    template_name = "posts/edit.html"  
    model = Post
    fields = ["title","subtitle","body","image"]  

    def test_func(self):                                #113
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  #113
    template_name = "posts/delete.html"  
    model = Post
    success_url = reverse_lazy('post_list')

    def test_func(self):                                #113
        obj = self.get_object()
        return obj.author == self.request.user




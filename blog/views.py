from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'  
    context_object_name = 'posts'  
    ordering = ['-created_at']  

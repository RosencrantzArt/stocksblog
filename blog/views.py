from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = 'posts'  
    ordering = ['-created_on']  

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')
 

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    context_object_name = 'post'

def home(request):
    return render(request, 'home.html')
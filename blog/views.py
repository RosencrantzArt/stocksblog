from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
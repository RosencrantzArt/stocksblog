from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from .models import Post, Comment
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = 'posts'
    ordering = ['-created_on']

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


def home(request):
    return render(request, 'home.html')


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_at")
    comment_count = comments.count()
    comment_form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect("post_detail", slug=post.slug)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval")
            return redirect("post_detail", slug=post.slug)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("post_detail", slug=post.slug)
        else:
            messages.error(request, "There was an error creating your post.")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully!")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted successfully!")
        return super().delete(request, *args, **kwargs)


@login_required
def comment_edit(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=post)
    if comment.author != request.user:
        messages.error(request, "You can only edit your own comments!")
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            updated_comment = comment_form.save(commit=False)
            updated_comment.post = post
            updated_comment.save()
            messages.success(request, "Comment updated successfully!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, "There was an error updating your comment.")
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        "blog/comment_edit.html",
        {"post": post, "comment_form": comment_form, "comment": comment},
    )


@login_required
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=post)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def approve_comment(request, comment_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to approve comments")
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.approved = True
    comment.save()
    messages.success(request, "Comment approved!")
    return redirect("post_detail", slug=comment.post.slug)

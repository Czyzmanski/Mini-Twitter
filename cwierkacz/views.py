from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from .models import Post


def index(request):
    latest_posts = Post.objects.order_by('-created_date')[:10]
    return render(request, 'cwierkacz/index.html', {'latest_posts': latest_posts})


def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'cwierkacz/post.html', {'post': post})


def show_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'cwierkacz/user.html', {'user': user})

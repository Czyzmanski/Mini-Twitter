from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from datetime import date

from .models import Post
from .forms import PostForm


def home(request):
    return redirect('posts/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = request.user
            text = form.cleaned_data.get('text')
            created_date = date.today()
            post = Post(author=author, text=text, created_date=created_date)
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'cwierkacz/new_post.html', {'form': form})


class PostsListView(generic.ListView):
    template_name = 'cwierkacz/posts.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_date')[:10]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'cwierkacz/post_detail.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'cwierkacz/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.post_set.all().order_by('-created_date')
        return context

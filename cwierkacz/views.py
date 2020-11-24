from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post


def home(request):
    return HttpResponseRedirect('posts/')


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
    pass


class IndexListView(generic.ListView):
    template_name = 'cwierkacz/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_date')[:10]


class PostDetailView(generic.DetailView):
    model = Post


class UserDetailView(generic.DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.post_set.all().order_by('-created_date')
        return context

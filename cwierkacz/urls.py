from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'cwierkacz'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', login_required(views.PostsListView.as_view()), name='posts'),
    path('posts/<int:pk>/', login_required(views.PostDetailView.as_view()), name='post-detail'),
    path('posts/new/', login_required(views.new_post), name='create-post'),
    path('users/', login_required(views.UsersListView.as_view()), name='users'),
    path('users/<int:pk>/', login_required(views.UserDetailView.as_view()), name='user-detail')
]

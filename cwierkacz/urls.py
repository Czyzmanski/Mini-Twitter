from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'cwierkacz'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', login_required(views.IndexListView.as_view()), name='index'),
    path('posts/<int:pk>/', login_required(views.PostDetailView.as_view()), name='post-detail'),
    #path('posts/new/', login_required(), name='create-post'),
    path('users/<int:pk>/', login_required(views.UserDetailView.as_view()), name='user-detail')
]

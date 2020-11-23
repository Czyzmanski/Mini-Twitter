from django.urls import path

from . import views

app_name = 'cwierkacz'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.show_post, name='show_post'),
    path('users/<int:user_id>/', views.show_user, name='show_user')
]

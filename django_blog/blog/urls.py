from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  
]

urlpatterns = [
     path('posts/<int:post_id>/comments/new/', views.comment_create, name='comment_create'),
    path('posts/<int:post_id>/comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('posts/<int:post_id>/comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, like_post, unlike_post, user_feed

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
    path('api/notifications/', include('notifications.urls')),

] + router.urls
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, user_feed

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
] + router.urls

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
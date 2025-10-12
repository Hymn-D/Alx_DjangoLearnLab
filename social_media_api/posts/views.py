from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer # type: ignore
from notifications.models import Notification # type: ignore
from django.contrib.contenttypes.models import ContentType

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    # Get all users the current user is following
    following_users = request.user.following.all()

    # Get posts from followed users, newest first
    feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    serializer = PostSerializer(feed_posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if already liked
    if Like.objects.filter(user=user, post=post).exists():
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    Like.objects.create(user=user, post=post)

    # Create notification
    if post.author != user:
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        )

    return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({'message': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
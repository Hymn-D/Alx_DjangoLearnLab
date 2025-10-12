from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, PostSerializer    # type: ignore
from .models import CustomUser
from django.conf import settings

User = settings.AUTH_USER_MODEL


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id) # type: ignore
    if user_to_follow == request.user:
        return Response({'error': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.followers.add(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id) # type: ignore
    if user_to_unfollow == request.user:
        return Response({'error': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.followers.remove(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)

def user_feed(request):

    following_users = request.user.following.all()
    feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at') # type: ignore

    serializer = PostSerializer(feed_posts, many=True)
    return Response(serializer.data)
from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),   
]

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  
]

urlpatterns = [
     path('auth/token/', obtain_auth_token, name='api_token_auth'),
  
]
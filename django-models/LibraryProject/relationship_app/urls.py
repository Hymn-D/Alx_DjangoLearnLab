from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]


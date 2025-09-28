from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),  # ✅ contains "add_book/"
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # ✅ contains "edit_book/"
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]





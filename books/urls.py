from django.urls import path

from . import views

urlpatterns = [
    path('book-list', views.book_list, name='book-list'),
    path('book/<str:key>/', views.book_detail, name='book-detail'),
    path('add-to-library/<str:key>/', views.add_to_library, name='add_to_library'),
]

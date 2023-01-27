from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    # path('book/<str:key>/', views.book_detail, name='book-detail'),
    # path('add-to-library/<str:book_id>/', views.add_to_library, name='add_to_library'),
]

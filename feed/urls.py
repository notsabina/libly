from django.urls import path

from .views import BookListView

urlpatterns = [
    path('/home/', BookListView.as_view(), name='home'),
]

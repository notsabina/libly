from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from books.models import Book


# Create your models here.

class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=40, blank=True)


# TODO add url creation

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)

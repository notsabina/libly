from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from books.models import Book


# Create your models here.

class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=40, blank=True)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, null=True)
    publication_date = models.CharField(max_length=32, null=True)
    num_pages = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2048, null=True)
    key = models.CharField(max_length=64, primary_key=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.author + " " + self.title + " " + self.key + " | PKey: " + str(self.pk)


class Library(models.Model):
    models.UniqueConstraint(fields=['user', 'book'], name="book_user_id", )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default= None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)

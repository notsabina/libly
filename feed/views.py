from django.views.generic import ListView

from books import models


class BookListView(ListView):
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    model = models.Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return models.Book.objects.all()


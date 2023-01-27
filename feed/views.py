from django.views.generic import ListView


class BookListView(ListView):
    template_name = 'feed/home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

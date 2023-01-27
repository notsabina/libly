from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # TODO add likes
        return context


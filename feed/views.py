from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    http_method_names = ["get"]
    template_name = "feed/homeview.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]
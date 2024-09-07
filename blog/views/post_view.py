from django.http import HttpResponse
from django.views import generic

from blog.models import Post


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Olá Terráqueos')


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

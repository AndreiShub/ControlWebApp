from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView


class HomeView(TemplateView):
    template_name = "blog/home.html"


class ListPosts(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "blog/blog.html"

class CreatePost(CreateView):
    model = Post
    fields = ["id","title","content","date_posted"]
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("posts")

class EditPost(UpdateView):
    model = Post
    template_name = "staffonly/edit_post.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("posts")


class DeletePost(DeleteView):
    model = Post
    template_name = "staffonly/delete_post.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts")
from django.urls import path
from ControlApp.views import ListPosts, HomeView, CreatePost

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("posts/", ListPosts.as_view(), name="posts"),
    path("create_post", CreatePost.as_view(), name="create_post")
]
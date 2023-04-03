from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
    path("count_words", views.count_words, name="count_words"),
    path("model_sample", views.model_sample, name="model_sample"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("post", views.posts, name="posts"),
    path("post/<str:pk>", views.post, name='post')
]

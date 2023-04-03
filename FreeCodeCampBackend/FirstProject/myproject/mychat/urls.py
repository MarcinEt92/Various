from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:chat_room>/", views.room, name="room"),
    path("check_view", views.check_view, name="check_view"),
    path("send", views.send, name="send"),
    path("get_messages/<str:room>", views.get_messages, name="get_messages"),
]

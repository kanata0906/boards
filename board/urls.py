from django.urls import path
from board import views

app_name = "board"

urlpatterns = [
    path("create/", views.create_thread, name="create_thread"),
    path("tweets/<int:thread_id>", views.tweet, name="tweets"),
]

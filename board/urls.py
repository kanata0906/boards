from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_thread, name="create_thread"),
    path("detail/<int:thread_id>/", views.detail, name="detail"),
    path("tweet/<int:thread_id>/", views.tweet, name="tweet"),
    path("delete/", views.delete_thread, name="delete_thread"),
]
from django.urls import path

from . import views


app_name = "dataGather"

urlpatterns = [
    path("", views.index, name="index"),
    # path("add_post", views.add_post, name="add_post"),
    # path("success/", views.success, name="success"),
    path("add_post/", views.AddPost.as_view(), name="add_post"),
]

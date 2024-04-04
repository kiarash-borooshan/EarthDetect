from django.urls import path

from . import views


app_name = "dataGather"

urlpatterns = [
    path("", views.index, name="index")
]
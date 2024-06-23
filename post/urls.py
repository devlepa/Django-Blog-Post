from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("post/details/<int:id>", views.details, name="details")
]
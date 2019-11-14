from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projectselect", views.projectselect, name="projectselect"),
    path("wpselect", views.wpselect, name="wpselect")
]
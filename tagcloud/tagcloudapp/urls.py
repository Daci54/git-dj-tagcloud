from django.urls import path
from .import views

urlpatterns = [
    # tagserfassen url and ajax requests
    path("", views.tagserfassen, name="tagserfassen"),
    path("projectselect", views.projectselect, name="projectselect"),
    path("wpselect", views.wpselect, name="wpselect"),
    path("test", views.test, name="test"),

    # tagsauswerten url and ajax requests
    path("tagsauswerten", views.tagsauswerten, name="tagsauswerten")
]
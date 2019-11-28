from django.urls import path
from django.views.generic import RedirectView
from .import views

urlpatterns = [
    # tagserfassen url and ajax requests
    path("", views.tagserfassen, name="tagserfassen"),
    path("projectselect", views.projectselect, name="projectselect"),
    path("wpselect", views.wpselect, name="wpselect"),
    path("tagsubmit", views.tagsubmit, name="tagsubmit"),

    # tagsauswerten url and ajax requests
    path("tagcloud", views.tagcloudchart, name="tagcloudchart"),
    path("tagquery", views.tagquery, name="tagquery")
]
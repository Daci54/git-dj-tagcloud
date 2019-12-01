from django.urls import path
from django.views.generic import RedirectView
from .import views

urlpatterns = [
    # tagserfassen url and ajax requests
    path("", views.tagserfassen, name="tagserfassen"),
    path("tagsubmit", views.tagsubmit, name="tagsubmit"), 

    # tagsauswerten url and ajax requests
    path("tagcloud", views.tagcloudchart, name="tagcloudchart"),
    path("tagquery", views.tagquery, name="tagquery"),

    # Login and Logout url
    path("login", views.loginpage, name="loginpage"),
    path("userlogin", views.userLogin, name="userlogin"),
    path("userlogout", views.userLogout, name="userlogout"),

    path("selectquery", views.selectquery, name="selectquery")
]
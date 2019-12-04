from django.urls import path
from .import views

urlpatterns = [
    #select and tagquery
    path("selectquery", views.selectquery, name="selectquery"),
    path("tagquery", views.tagquery, name="tagquery"),

    # tagsubmit url and ajax requests
    path("", views.tagserfassen, name="tagserfassen"),
    path("tagsubmit", views.tagsubmit, name="tagsubmit"), 

    # tagcloud url and ajax requests
    path("tagcloud", views.tagcloudchart, name="tagcloudchart"),

    # ranking url and ajax requests
    path("ranking", views.rankingchart, name="ranking"),
    path("tagcountcreated", views.tagcountcreatedquery, name="tagcountcreated"),
    path("tagcountsubmitted", views.tagcountsubmittedquery, name="tagcountsubmitted"),

    # Login and Logout url
    path("login", views.loginpage, name="loginpage"),
    path("userlogin", views.userLogin, name="userlogin"),
    path("logout", views.userLogout, name="userlogout")
]
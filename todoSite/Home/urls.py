from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout, name="logout"),
    path("additem", views.addItem, name="addItem"),
    path("delitem", views.deleteItem, name="delitem")
]
from django.contrib import admin
from django.urls import path
from .views import note_list, note_create, note_detail


urlpatterns = [
    path("", note_list, name="note_list"),
    path("list/", note_list, name="note_list"),
    path("create/", note_create,name="note_create"),
    path("list/<int:pk>/", note_detail, name="note_detail")]
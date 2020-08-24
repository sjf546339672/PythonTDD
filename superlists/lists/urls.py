# coding: utf-8
from django.urls import path
from .views import home_page

urlpatterns = [
    path(r"home/", home_page, name="home"),
]


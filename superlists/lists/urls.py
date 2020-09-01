from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import home_page

urlpatterns = [
    path(r"^$", view=home_page, name="home")
]

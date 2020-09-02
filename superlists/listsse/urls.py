from django.urls import path

from .views import home_page, index

urlpatterns = [
    path("home/", home_page, name="home"),
    path("index/", index, name="index")
]

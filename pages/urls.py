from django.urls import path
from .views import HomePageView, AboutPageView, home_func_view

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("home/", home_func_view, name='home2'),
]
from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.feed, name="feed"),
    path('profile/', views.profile, name="profile"),


]
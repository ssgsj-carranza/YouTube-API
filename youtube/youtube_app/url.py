from django.urls import path
from . import views

urlpatterns = [
    path('youtube_app', views.PageMethods.as_view())
]
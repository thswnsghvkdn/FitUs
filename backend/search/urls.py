from django.urls import path
from search import views

urlpatterns = [path("size/", views.size_search)]


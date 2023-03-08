from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('getall', views.getAllBooks, name = "getBooks"),
    path('add', views.addBook, name = "add")
]

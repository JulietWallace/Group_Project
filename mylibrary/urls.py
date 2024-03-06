from django.urls import path
from mylibrary import views
from django.contrib import admin

app_name = 'mylibrary'


urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
]
from django.urls import path
from mylibrary import views
from django.contrib import admin

app_name = 'mylibrary'


urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<slug:book_name_slug>/', views.show_book, name='show_book'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('mygoals/', views.mygoals, name='mygoals'),
    path('set_goal/', views.mygoals, name='set_goal'),

]
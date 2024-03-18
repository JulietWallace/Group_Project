from django.urls import path
from mylibrary import views
from django.contrib import admin

app_name = 'mylibrary'


urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<slug:book_name_slug>/', views.show_book, name='show_book'),
    path('about/', views.about, name='about'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('mygoals/', views.mygoals, name='mygoals'),
    path('setgoal/', views.setgoal, name='setgoal'),
    path('mygoals/<slug:goal_slug>/', views.show_goal, name='show_goal'),

]
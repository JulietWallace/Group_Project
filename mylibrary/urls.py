from django.urls import path
from mylibrary import views
from django.contrib import admin

app_name = 'mylibrary'


urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<slug:book_name_slug>/', views.show_book, name='show_book'),
    path('book/<slug:slug>/write_review/', views.write_review, name='write_review'),
    path('about/', views.about, name='about'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('mygoals/', views.mygoals, name='mygoals'),
    path('myreviews/', views.myreviews, name='myreviews'),
    path('search_results/', views.search_results, name='search_results'),
    path('set_goal/', views.set_goal, name='set_goal'),
    path('add_category/', views.add_category, name='add_category'),
    path('search/', views.search, name='search'),
    path('explorecategory/', views.explorecategory, name='explorecategory'),
    path('category/<slug:category_name_slug>', views.show_category, name='show_category'),
    path('logout/', views.user_logout, name='logout'),


]
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
<<<<<<< HEAD
    path('myreviews/', views.myreviews, name='myreviews'),
    path('explorecategory/', views.explorecategory, name='explorecategory'),
    path('category/<slug:category_name_slug>', views.show_category, name='show_category'),
    path('set_goal/', views.mygoals, name='set_goal'),
    path('logout/', views.user_logout, name='logout'),
=======
    path('setgoal/', views.setgoal, name='setgoal'),
    path('mygoals/<slug:goal_slug>/', views.show_goal, name='show_goal'),
>>>>>>> 60649341eddbe63f2cbea2418a8bc12987723101

]
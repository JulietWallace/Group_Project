from django.urls import path 
from mylibrary import views
app_name = 'mylibrary'


urlpatterns = [
    path('', views.index, name='index'),
]
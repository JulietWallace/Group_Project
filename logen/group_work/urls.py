"""group_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from mylibrary import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('mylibrary/', include('mylibrary.urls')),
    path('category/<slug:category_name_slug>/', views.show_category, name = "show_category"),
    path('mylibrary/book/<slug:book_name_slug>/', views.show_book, name='show_book'),
    path('myreviews/', views.myreviews, name='myreviews'),
    path('register/', views.register, name='register'),
    path("admin/", admin.site.urls),
]

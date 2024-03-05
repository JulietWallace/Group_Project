from django.db import models

# Create your models here.


from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    categoryID=models.CharField(max_length=20, unique=True)
    numOfBooks=models.IntegerField(default=0)


class Review(models.Model):
    reviewID=models.CharField(max_length=50, unique=True)
    dateWritten=models.DateField()
    edited=models.BooleanField(default=False)
    reviewAuthorFK=models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Group(models.Model):
    numOfMembers=models.IntegerField(default=0)
    groupID=models.CharField(max_length=50)
    groupMember=models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField()
    profilePic=models.ImageField()
    password=models.CharField(max_length=20)

class Book(models.Model):
    ISBN=models.IntegerField(unique=True)
    author=models.CharField()
    uploadedBy=models.ForeignKey(User, on_delete=models.CASCADE)
    coverPhoto=models.ImageField()

class Goal(models.Model):
    goalAuthor=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    dateSet=models.DateTimeField()
    achieved=models.BooleanField()
    goalID=models.CharField(max_length=50,unique=True)


class Admin(models.Model):
    adminID=models.CharField(50, unique=True) 

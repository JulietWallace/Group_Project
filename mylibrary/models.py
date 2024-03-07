from django.db import models

# Create your models here.
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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileLink = models.URLField(blank=True)
    profilePic=models.ImageField()


class Book(models.Model):
    ISBN=models.IntegerField(unique=True)
    author=models.CharField(max_length=50)
    uploadedBy=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    coverPhoto=models.ImageField()
    categories = models.ManyToManyField(Category)
    title=models.CharField(max_length=500)
    slug=models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Book,self).save(*args, **kwargs)


class Goal(models.Model):
    goalAuthor=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    dateSet=models.DateTimeField()
    achieved=models.BooleanField()
    goalID=models.CharField(max_length=50,unique=True)


class Admin(models.Model):
    adminID=models.CharField(max_length=50, unique=True) 

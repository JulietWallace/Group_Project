from django.db import models

# Create your models here.
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    categoryID=models.CharField(max_length=20, unique=True)
    numOfBooks=models.IntegerField(default=0)
    slug=models.SlugField(unique = True)

    def __str__(self):
        return self.categoryID
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryID)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Categories'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileLink = models.URLField(blank=True)
    profilePic=models.ImageField(upload_to='profile_images', blank = True)

    #def save(self, *args, **kwargs):
        #if not self.slug:
        #self.slug = slugify(self.name)
    #super().save(*args, **kwargs)
    
        #super(Book,self).save(*args, **kwargs)


class Book(models.Model):
    ISBN=models.IntegerField(unique=True)
    author=models.CharField(max_length=50)
    uploadedBy=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    coverPhoto=models.ImageField()
    categories = models.ManyToManyField(Category)
    title=models.CharField(max_length=500)
    slug=models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Book,self).save(*args, **kwargs)

class Goal(models.Model):
    goalName=models.CharField(max_length=500,null=True, unique=True)
    goalAuthor=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    dateSet=models.DateTimeField()
    achieved=models.BooleanField()
    ISBN=models.IntegerField()
    numPages=models.IntegerField(null=True)
    dateDay=models.IntegerField(null=True)
    dateMonth=models.IntegerField(null=True)
    dateYear=models.IntegerField(null=True)
    slug=models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.goalName)
        super(Goal,self).save(*args, **kwargs)


class Admin(models.Model):
    adminID=models.CharField(max_length=50, unique=True) 

class Review(models.Model):
    reviewID=models.CharField(max_length=50, unique=True)
    message=models.CharField(max_length=50, unique=True)
    dateWritten=models.DateField(auto_now_add=True)
    edited=models.BooleanField(default=False)
    reviewAuthorFK=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reviewBookFK=models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message




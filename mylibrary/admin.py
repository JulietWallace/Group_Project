from django.contrib import admin
from mylibrary.models import Book, Category, Review, UserProfile, Goal, Admin, BooksUserReading

# Register your models here.


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Goal)
admin.site.register(BooksUserReading)

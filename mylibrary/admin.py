from django.contrib import admin
from mylibrary.models import Book, Category, Review, User, Goal, Admin

# Register your models here.


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Goal)

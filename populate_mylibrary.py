from django.http import HttpResponse
import django
from django.shortcuts import render
from mylibrary.forms import BookForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'group_work.settings')


django.setup() 

from mylibrary.models import Book, Category, Review, User, Goal, Admin

def populate():
    book_dict=[{"title":"Pride and Prejudice", "author": "Jane Austen", "ISBN": 9780140430721},
               {"title":"Crime and Punishment", "author": "Fyodor Dostoyevsky", "ISBN": 648103837163},
               {"title":"War and Peace", "author": "Leo Tolstoy", "ISBN": 4567891234},
               {"title":"1984", "author": "George Orwell", "ISBN": 435678129391}]
    for b in book_dict:
        add_book(b["title"], b["ISBN"], b["author"])
    for book in Book.objects.all():
        print(book.title)

    

def add_book(title, ISBN, author):
    book=Book.objects.get_or_create(title=title, ISBN=ISBN, author=author)[0]
    book.save()
    return book

if __name__=='__main__':
    print('Population script running...') 
    populate()
import django

# Create your views here.

import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"group_work.settings")


django.setup() 

from mylibrary.models import Book, Category, Review, User, Goal, Admin

def populate():
    book_dict=[{"title":"Pride and Prejudice", "author": "Jane Austen", "ISBN": 9780140430721, "uploadedBy":"juliet"},
               {"title":"Crime and Punishment", "author": "Fyodor Dostoyevsky", "ISBN": 648103837163, "uploadedBy":"juliet"},
               {"title":"War and Peace", "author": "Leo Tolstoy", "ISBN": 4567891234, "uploadedBy":"juliet"},
               {"title":"1984", "author": "George Orwell", "ISBN": 435678129391, "uploadedBy":"juliet"}]
    for b in book_dict:
        add_book(b["title"], b["ISBN"], b["author"],b["uploadedBy"])
    for book in Book.objects.all():
        print(book.title)

    

def add_book(title, ISBN, author, uploadedBy):
    book=Book.objects.get_or_create(title=title, ISBN=ISBN, author=author,uploadedBy=uploadedBy)[0]
    book.save()
    return book

if __name__=='__main__':
    print('Population script running...') 
    populate()
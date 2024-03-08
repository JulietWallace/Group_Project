from django.shortcuts import render
from mylibrary.forms import BookForm
from django.shortcuts import redirect
import django
from django.urls import reverse
# Create your views here.

from django.http import HttpResponse 
from mylibrary.models import Book, Category, Review, User

def index(request):
    return render(request, 'mylibrary/index.html', context={})

def myprofile(request):
    return render(request, 'mylibrary/myprofile.html', context={})


def mygoals(request):
    return render(request, 'mylibrary/mygoals.html', context={})

def show_book(request, book_name_slug):
    context_dict={}
    try:
        book=Book.objects.get(slug=book_name_slug)
        context_dict["book"]=book
    except Book.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request, "rango/book.html", context=context_dict)

def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form =  BookForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.uploadedBy=request.user
            book.save()
            show_book(request, book.slug)
            return redirect(reverse('mylibrary:show_book', kwargs={'book_name_slug': book.slug}))
        else:
            print(form.errors)
    
    return render(request, 'mylibrary/add_book.html', {'form': form})

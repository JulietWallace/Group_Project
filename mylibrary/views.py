from django.shortcuts import render
from mylibrary.forms import BookForm
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse 

def index(request):
    return HttpResponse("Welcome to MyLibrary")


def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form =  BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/mylibrary/')
        else:
            print(form.errors)
    
    return render(request, 'mylibrary/add_book.html', {'form': form})

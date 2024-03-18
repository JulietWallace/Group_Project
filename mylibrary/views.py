from django.shortcuts import render
from mylibrary.forms import BookForm, UserForm, GoalForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import django
from django.urls import reverse
import datetime
# Create your views here.

from django.http import HttpResponse 
from mylibrary.models import Book, Category, Review, User, Goal

def index(request):
    return render(request, 'mylibrary/index.html', context={})

def myprofile(request):
    user = User.objects.get(username=request.user.username)
    context_dict={"user":user}
    return render(request, 'mylibrary/myprofile.html', context_dict)


def set_goal(request):
    form = GoalForm()

    if request.method == 'POST':
        goal =  BookForm(request.POST)
        if form.is_valid():
            goal=form.save(commit=False)
            goal.goalAuthor=request.user
            goal.dateSet=datetime.datetime.now()
            goal.save()
            return redirect(reverse('mylibrary:mygoals'))
        else:
            print(form.errors)
    
    return render(request, 'mylibrary/mygoals.html', {'form': form})

@login_required
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profilePic' in request.FILES:
                profile.picture = request.FILES['profilePic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, "mylibrary/register.html", context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
        
def user_login(request):

def mygoals(request):
    context_dict={}
    goals = Goal.objects.filter(goalAuthor=request.user)
    context_dict["goals"] = goals
    return render(request, "mygoals.html", context=context_dict)

def show_book(request, book_name_slug):
    context_dict={}
    try:
        book=Book.objects.get(slug=book_name_slug)
        context_dict["book"]=book
    except Book.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request, "mylibrary/book.html", context=context_dict)

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

def about(request):
    return render(request, 'mylibrary/about.html', context={})



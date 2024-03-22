from django.shortcuts import render
from mylibrary.forms import BookForm, UserProfileForm, UserForm, ReviewForm, GoalForm, CategoryForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import django
from django.urls import reverse
import datetime
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse 
from mylibrary.models import Book, Category, Review, User, Goal, UserProfile

def index(request):
    category_list = Category.objects.all()
    context_dict = {}
    book_list = Book.objects.order_by('-title')[:3]
    context_dict['book0'] = book_list[0]
    context_dict['book1'] = book_list[1]
    context_dict['book2'] = book_list[2]
    return render(request, 'mylibrary/index.html', context_dict)

def search(request):
    books = Book.objects.filter(title__icontains=request.GET.get('search'))
    context_dict = {}
    context_dict['books'] = books

    return render(request, 'mylibrary/search_results.html', context_dict)

def search_results(request):
    results = {}
    return render(request, 'mylibrary/search_results.html', {'results': results})    

def search(request):
    #results = Book.objects.filter(name__icontains=query)
    books = Book.objects.filter(title__icontains=request.GET.get('search'))
    context_dict = {}
    context_dict['books'] = books

    return render(request, 'mylibrary/search_results.html', context_dict)

def search_results(request):
    #results = Book.objects.filter(name__icontains=query)
    print(results)
    results = {}
    return render(request, 'mylibrary/search_results.html', {'results': results})    

def myprofile(request):
    user = User.objects.get(username=request.user.username)
    context_dict = {}
    context_dict['user'] = user
    context_dict={"user":user}
    return render(request, 'mylibrary/myprofile.html', context_dict)

def write_review(request, slug):

    form = ReviewForm()
    book = Book.objects.filter(slug = slug).first()

    if request.method == 'POST':
        form =  ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.reviewID = book.slug + str(request.user) + str(review.message)
            review.reviewAuthorFK=request.user
            review.reviewBookFK = Book.objects.filter(slug = slug).first()
            review.save()
            return redirect('myreviews')
        else:
            form = ReviewForm()
            print(form.errors)
    
    return render(request, 'mylibrary/write_review.html', {'form': form, 'book':book})


def explorecategory(request):

    #book_list = Book.objects.order_by('-likes')[:5]
    book_list = Book.objects.all()
    category_list = Category.objects.all()
    context_dict = {}
    context_dict['categories'] = category_list
    #context_dict['books'] = book_list
    #context_dict['book'] = book_list
    print(context_dict)
    #context_dict['book'] = book_list

    #images = Book.
    return render(request, 'mylibrary/explorecategory.html', context = context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method =='POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect()
        else:
            print(form.errors)
    return render(request, 'mylibrary/add_category.html', {'form':form})
    

def user_login(request):
    if request.method ==  'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('mylibrary:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"invalid login details:{username}, {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'mylibrary/login.html', {})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit = False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, "mylibrary/register.html", context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def set_goal(request):
    form = GoalForm()

    if request.method == 'POST':
        goal =  BookForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.goalAuthor=request.user
            form.dateSet=datetime.datetime.now()
            form.save()

        else:
            print(form.errors)
    
    return render(request, "mylibrary/set_goal.html", {'form': form})

def mygoals(request):
    context_dict={}
    goals = Goal.objects.filter(goalAuthor=request.user)
    context_dict["goals"] = goals
    return render(request, "mylibrary/mygoals.html", context=context_dict)

def myreviews(request):
    context_dict={}
    review = Review.objects.filter(reviewAuthorFK=request.user)
    context_dict["reviews"] = review
    return render(request, "mylibrary/myreviews.html", context=context_dict)

def show_book(request,book_name_slug):
    context_dict={}
    try:
        book=Book.objects.get(slug=book_name_slug)
        review=Review.objects.filter(reviewBookFK=book)
        categories = book.categories.all()
        #user=User.objects.filter(reviewAuthorFK= user)
        context_dict={}
        context_dict["book"]=book
        context_dict["reviews"]=review
        context_dict["categories"]=categories
        print(categories)
        #context_dict["users"]=user
    except Book.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request, "mylibrary/book.html", context=context_dict)

def current_book(request):
        return render(request, "mylibrary/book.html", context=context_dict)

def curr_books(request):
    context_dict={}
    context_dict['books'] = BooksUserReading.objects.filter(userFK=UserProfile.objects.get(user=request.user))
    return render(request, "mylibrary/currentbooks.html", context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        books = Book.objects.filter(categories = category)
        print(books)

        context_dict['books'] = books
        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['books'] = None

    return render(request, 'mylibrary/category.html', context=context_dict)

def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form =  BookForm(request.POST, request.FILES)
        if form.is_valid():
            book=form.save(commit=False)
            book.uploadedBy=request.user
            categories = form.cleaned_data['categories']
            if 'photoCover' in request.FILES:
                book.photoCover = request.FILES['photoCover']
            book.save()
            book.categories.set(categories)
            show_book(request, book.slug)
            return redirect(reverse('mylibrary:show_book', kwargs={'book_name_slug': book.slug}))
        else:
            print(form.errors)
    
    return render(request, 'mylibrary/add_book.html', {'form': form})

def about(request):
    return render(request, 'mylibrary/about.html', context={})

class user_read_book(View):
    def get(self,request):
        bookISBN = request.GET['bookISBN'] 
        book = Book.objects.get(ISBN=int(bookISBN))
        userID = request.GET['user']
        user = User.objects.get(username = userID)
        userProfile = UserProfile.objects.get(user = user)
        object = BooksUserReading.objects.get_or_create(userFK=userProfile,bookFK=book)[0]
        object.userFK=userProfile
        object.bookFK=book
        object.pagesRead = 0
        object.startedReading = datetime.datetime.now
        #object.save()
        return HttpResponse("Hello")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('mylibrary:index'))


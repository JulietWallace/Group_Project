from django.shortcuts import render
from mylibrary.forms import BookForm, UserProfileForm, UserForm, ReviewForm
from mylibrary.forms import BookForm, GoalForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import django
from django.urls import reverse
import datetime
from django.views import View
# Create your views here.

from django.http import HttpResponse 
from mylibrary.models import Book, Category, Review, User, Goal, UserProfile, BooksUserReading

def index(request):
    category_list = Category.objects.all()
    context_dict = {}
    print("YOUR MOM") 
    print((category_list))
    context_dict['categories'] = category_list
    return render(request, 'mylibrary/index.html', context={})

def myprofile(request):
    print(request.user)
    user = User.objects.get(username=request.user)
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
    print("YOUR MOM")
    print((category_list))
    context_dict['categories'] = category_list
    #context_dict['book'] = book_list
    print(context_dict)
    #context_dict['book'] = book_list

    #images = Book.
    return render(request, 'mylibrary/explorecategory.html', context = context_dict)
    

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


def setgoal(request):
    form = GoalForm()

    if request.method == 'POST':
        goal =  GoalForm(request.POST)
        if form.is_valid():
            print("valid")
            goal=form.save(commit=False)
            goal.goalAuthor=request.user
            goal.dateSet=datetime.datetime.now()
            goal.save()
            return redirect(reverse('mylibrary:show_goal', kwargs={'goal_slug': goal.slug}))
        else:
            print("form errors")
            print(form.errors)
    
    return render(request, 'mylibrary/setgoal.html', {'form': form})

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

def book(request,book_name_slug):
    context_dict={}
    try:
        book=Book.objects.get(slug=book_name_slug)
        review=Review.objects.filter(reviewBookFK=book) #maybe add in an order by feature
        context_dict={}
        context_dict["book"]=book
        context_dict["reviews"]=review
        #context_dict['readingList']=UserProfile.objects.get(user=request.user).books_reading
        context_dict["user"] = UserProfile.objects.get(user=request.user)
    except Book.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
        context_dict['readingList']=None
    return render(request, "mylibrary/book.html", context=context_dict)

def curr_books(request):
    context_dict={}
    context_dict['books']=[]
    context_dict['books'] = BooksUserReading.objects.filter(userFK=request.user)
    return render(request, "mylibrary/currentbooks.html", context=context_dict)



def show_book(request, book_name_slug):
    context_dict={}
    try:
        book=Book.objects.get(slug=book_name_slug)
        review=Review.objects.filter(reviewBookFK=book)
        context_dict={}
        context_dict["book"]=book
        context_dict["reviews"]=review
    except Book.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request, "mylibrary/book.html", context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        books = Book.objects.filter(categories=category)
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
        form =  BookForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.uploadedBy=request.user
            book.save()
            #show_book(request, book.slug)
            return redirect(reverse('mylibrary:show_book', kwargs={'book_name_slug': book.slug}))
        else:
            print(form.errors)
    
    return render(request, 'mylibrary/add_book.html', {'form': form})

def about(request):
    return render(request, 'mylibrary/about.html', context={})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('mylibrary:index'))

def show_goal(request, goal_slug):
    context_dict={}
    try:
        goal=Goal.objects.get(slug=goal_slug)
        context_dict["goal"]=goal
    except Goal.DoesNotExist:
        context_dict["goal"]=None
    return render(request, "mylibrary/goal.html", context=context_dict) 

class LikeCategoryView(): #Taken from tango with django
    def get(self, request):
        category_id = request.GET['category_id'] 
        try:
            category = Category.objects.get(id=int(category_id)) 
        except Category.DoesNotExist:
            return HttpResponse(-1) 
        except ValueError:
            return HttpResponse(-1) 
        category.likes = category.likes + 1
        category.save()
        return HttpResponse(category.likes)
    
#This should add book to the user's reading list when they click the button
class BookReadView(View): 
    def get(self, request):
        user=UserProfile.objects.get(user=request.user)
        book_ISBN = request.GET['ISBN']
        book = Book.objects.get(ISBN = book_ISBN) 
        obj = BooksUserReading(user,book)
        book.users_reading.append(user)
        user.books_reading.append(book)
        book.save()
        user.save()
        obj.save()
        return HttpResponse(user.books_reading)



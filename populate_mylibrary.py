import django

# Create your views here.

import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"group_work.settings")


django.setup() 

from mylibrary.models import Book, Category, Review, User, Goal, Admin

counter = 0

def populate():
    
    user_dict = [{"username":"dylan"}, {"username":"dylan1"}]
    category_dict = [{"categoryID": "Classic", "numOfBooks" : 10}, {"categoryID": "History", "numOfBooks" : 2}, {"categoryID":"Fantasy","numOfBooks":4},{"categoryID":"Action","numOfBooks":4}]
    
    for u in user_dict:
        add_user(u["username"])
        
    book_dict=[{"title":"Pride and Prejudice", "author": "Jane Austen", "ISBN": 9780140430721, "uploadedBy":User.objects.get(username="dylan"), "categories":{"History"}, "coverPhoto":"book_images/bookimg1.jpg"},
               {"title":"Crime and Punishment", "author": "Fyodor Dostoyevsky", "ISBN": 648103837163, "uploadedBy":User.objects.get(username="dylan"),"categories":{"History"},"coverPhoto":"book_images/bookimg2.jpg"},
               {"title":"War and Peace", "author": "Leo Tolstoy", "ISBN": 4567891234, "uploadedBy":User.objects.get(username="dylan"),"categories":{"History"}, "coverPhoto":"book_images/bookimg3.jpg"},
               {"title":"1984", "author": "George Orwell", "ISBN": 435678129391, "uploadedBy":User.objects.get(username="dylan"),"categories":{"History"}, "coverPhoto":"book_images/bookimg4.jpg"}]
    
    Fbook_dict=[{"title":"The Blade Itself", "author": "Joe Abercrombie", "ISBN": 900001, "uploadedBy":User.objects.get(username="dylan"),"categories":{"Action", "Fantasy"}, "coverPhoto":"book_images/bookimg20.jpg"},
               {"title":"The Last Argument of Kings", "author": "Joe Abercrombie", "ISBN": 900002, "uploadedBy":User.objects.get(username="dylan"), "categories":{"Action", "Fantasy"}, "coverPhoto":"book_images/bookimg7.jpg"},
               {"title":"The Wisdom of Crowds", "author": "Joe Abercrombie", "ISBN": 45678912332, "uploadedBy":User.objects.get(username="dylan"), "categories":{"Action", "Fantasy"}, "coverPhoto":"book_images/bookimg0.png"},
               {"title":"The Heroes", "author": "Joe Abercrombie", "ISBN": 4356781229391, "uploadedBy":User.objects.get(username="dylan"), "categories":{"Action", "Fantasy"},"coverPhoto":"book_images/bookimg8.jpg"}]
    
    for c in category_dict:
        add_category(c["categoryID"], c["numOfBooks"])
    for b in book_dict:
        add_book(b["title"], b["ISBN"], b["author"],b["uploadedBy"], b["categories"], b["coverPhoto"])
    for b in Fbook_dict:
        add_book(b["title"], b["ISBN"], b["author"],b["uploadedBy"], b["categories"], b["coverPhoto"])
    for u in user_dict:
        add_user(u["username"])
    review_dict = [{"reviewID" : "asd","message": " bad book", "reviewAuthorFK": User.objects.get(username="dylan"), "reviewBookFK":Book.objects.get(ISBN = 900001)}]
    review_dict = [{"reviewID" : "asd","message": " Utter Garbage", "reviewAuthorFK": User.objects.get(username="dylan"), "reviewBookFK":Book.objects.get(ISBN = 900002)}]
    for r in review_dict:
        add_review(r["reviewID"], r["message"], r["reviewAuthorFK"], r["reviewBookFK"],)

    #add_book("title", 54, "author", User.objects.get(username="dylan"))
        for book in Book.objects.all():
            print(book.title)
        #for c in category_dict:
            #book.categories.add(Category.objects.get(categoryID = "Action"))

    

def add_book(title, ISBN, author, uploadedBy, categories, coverPhoto):
    book=Book.objects.get_or_create(title=title, ISBN=ISBN, author=author,uploadedBy=uploadedBy, coverPhoto = coverPhoto)[0]
    book.save()
    for category in categories:
        print(category)
        book.categories.add(Category.objects.get(categoryID = category))

    return book

def add_category(categoryID, numOfBooks):
    print(categoryID)
    category =Category.objects.get_or_create(categoryID = categoryID, numOfBooks = numOfBooks)[0]
    category.save()
    return category

def add_review(reviewID, message, reviewAuthorFK, reviewBookFK):
    review =Review.objects.get_or_create(reviewID= reviewID, message = message, reviewAuthorFK = reviewAuthorFK, reviewBookFK=reviewBookFK)[0]
    review.save()
    return review

def add_user(username):
    user = User.objects.get_or_create(username=username)[0]
    user.save()
    return user

if __name__=='__main__':
    print('Population script running...') 
    populate()
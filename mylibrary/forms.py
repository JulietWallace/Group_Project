from django import forms
from mylibrary.models import Book, Category, Review, User, Goal, Admin
from django.contrib.auth.models import User 



class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter the title of the book")
    author = forms.CharField(max_length=50, help_text="Enter the author of the book")
    ISBN = forms.IntegerField(help_text="Enter the ISBN of the book")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    book_dict = {"title": title, "author": author,"ISBN":ISBN, "uploadedBy":None}
    
    class Meta:
        model = Book
        fields=('title', 'author','ISBN','uploadedBy')

    def set_uploaded_by(self, user):
        self.book_dict["uploadedBy"]=user

    def get_book_dict(self):
        return self.book_dict

class GoalForm(forms.ModelForm):
    ISBN = forms.IntegerField(help_text="Enter the ISBN of the book this goal refers to")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    numPages=forms.IntegerField(help_text="How many pages do you want to read?")
    dateDay=forms.IntegerField(help_text="When do you want to achieve this by? Day: ")
    dateMonth=forms.IntegerField(help_text="Month: ")
    dateYear=forms.IntegerField(help_text="Year: ")
    goalName=forms.CharField(help_text="Type a name for your goal:")

    
    class Meta:
        model = Goal
        fields=('goalAuthor', 'dateSet', 'slug', 'dateDay', 'dateMonth', 'dateYear','goalName', 'ISBN')



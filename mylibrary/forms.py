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
    title = forms.CharField(max_length=128, help_text="Enter the title of the book")
    author = forms.CharField(max_length=50, help_text="Enter the author of the book")
    ISBN = forms.IntegerField(help_text="Enter the ISBN of the book")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    goal_dict = {"goalAuthor": title, "dateSet": author,"goalID":ISBN, "achieved":None}
    
    class Meta:
        model = Goal
        fields=('goalAuthor', 'dateSet','goalID','achieved')

    def set_goalAuthor(self, user):
        self.goal_dict["goalAuthor"]=user



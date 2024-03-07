from django import forms
from mylibrary.models import Book, Category, Review, User, Goal, Admin
from django.contrib.auth.models import User 



class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter the title of the book")
    author = forms.CharField(max_length=50, help_text="Enter the author of the book")
    ISBN = forms.IntegerField(help_text="Enter the ISBN of the book")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Book

        fields=('title', 'author','ISBN',)

    def set_uploaded_by(self, user):
        self.uploadedBy.id = user

from django import forms
from mylibrary.models import Book, Category, Review, UserProfile, Goal, Admin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ngettext



class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter the title of the book")
    author = forms.CharField(max_length=50, help_text="Enter the author of the book")
    ISBN = forms.IntegerField(help_text="Enter the ISBN of the book")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), help_text="Select the category for the book")
    book_dict = {"title": title, "author": author,"ISBN":ISBN, "uploadedBy":None}
    
    class Meta:
        model = Book
        fields=('title', 'author','ISBN', 'categories')

    def set_uploaded_by(self, user):
        self.book_dict["uploadedBy"]=user

    def get_book_dict(self):
        return self.book_dict
    
class ReviewForm(forms.ModelForm):
    message = forms.CharField(max_length=128, help_text="Write review")
    review_dict = {"message": message}
    
    class Meta:
        model = Review
        fields=('message', )

    def set_reviewAuthor(self, user):
        self.review_dict["reviewAuthor"] = user


class GoalForm(forms.ModelForm):
    ISBN = forms.IntegerField(help_text="Enter the ISBN of the book this goal refers to")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    numPages=forms.IntegerField(help_text="How many pages do you want to read?")
    dateDay=forms.IntegerField(help_text="When do you want to achieve this by? Day: ")
    dateMonth=forms.IntegerField(help_text="Month: ")
    dateYear=forms.IntegerField(help_text="Year: ")

    
    class Meta:
        model = Goal
        fields=('goalAuthor', 'dateSet','goalID','achieved', 'slug', 'dateDay', 'dateMonth', 'dateYear')


class MinimumLengthValidator:
    """
    Validate whether the password is of a minimum length 8.
    """
    def __init__(self, min_length=8):
        self.min_length = min_length
 
    def __call__(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "This password is too short. It must contain at least %(min_length)d character.",
                    "This password is too short. It must contain at least %(min_length)d characters.",
                    self.min_length
                    ),
                    code='password_too_short',
                    params={'min_length': self.min_length},
                )
        
    def get_help_text(self):
        return (
            "Your password must contain at least %(min_length)d characters."
            % {'min_length': self.min_length}
        )
            
class NumericPasswordValidator:
    """
    Validate whether the password is alphanumeric.
    """
    def __call__(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("This password is entirely numeric."),
                code='password_entirely_numeric',
            )
            
class LettersPasswordValidator:
            
    def __call__(self, password, user=None):
        if password.isalpha():
            raise ValidationError(
                "This password is entirely composed of letters.",
                code='password_entirely_letters',
            )
 
def get_help_text(self):
        return _("Your password can't be entirely numeric. It has to contain at least one uppercase letter, one lower case, a number and symbol")

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), validators=[MinimumLengthValidator(8),
                                                                          LettersPasswordValidator(), NumericPasswordValidator()])
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profilePic',)

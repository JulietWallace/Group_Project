from django.test import TestCase
from django.db import IntegrityError
from .models import Book, Category

class Test(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(categoryID='cat1')
        self.category2 = Category.objects.create(categoryID='cat2')
        self.book = Book.objects.create(ISBN = 2, author = "a", title = "a")
        self.book1 = Book.objects.create(ISBN = 1, author = "b", title = "b")
        self.book.save()
        self.book.categories.add(self.category1, self.category2)
        self.book1.categories.add(self.category1)
        print(self.book)
        print(self.book)

    def test_CategoryInBookTest(self):
        book = Book.objects.get(ISBN = 2)
        self.assertTrue(book.categories.count() > 1)

    def test_BookInCategory(self):
        category = Category.objects.get(categoryID='cat1')
        books = Book.objects.filter(categories = category)

        self.assertTrue(books.count() > 1)

    def test_CategoryIsUnique(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(categoryID='cat2')
    def test_ISBNIsUnique(self):
        with self.assertRaises(IntegrityError):
            Book.objects.create(ISBN = 2, author = "a", title = "a")


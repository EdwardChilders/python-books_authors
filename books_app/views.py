from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    context = {
        'authors': Author.objects.all(),
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def view_book(request, book_id):
    context = {
        'book_viewed': Book.objects.get(id=book_id),
        'auth_of': Author.objects.all()
    }
    return render(request, 'book.html', context)


def add_book(request):
    print(request.POST)
    Book.objects.create(
        title=request.POST['title_of_book'],
        desc=request.POST['description']
    )
    return redirect('/')


def add_auth_to_book(request):
    print(request.POST)
    auth = Author.objects.get(id=request.POST['auth_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    book.authors.add(auth)
    return redirect(f'/view_book/{book.id}')


def authors(request):
    context = {
        'authors': Author.objects.all(),
        'books': Book.objects.all()
    }
    return render(request, 'authors.html', context)


def add_author(request):
    print(request.POST)
    Author.objects.create(
        first_name=request.POST['fname_of_author'],
        last_name=request.POST['lname_of_author'],
        notes=request.POST['notes_of_author']
    )
    return redirect('/authors')


def view_auth(request, auth_id):
    context = {
        'auth_viewed': Author.objects.get(id=auth_id),
        'book_of': Book.objects.all()
    }
    return render(request, 'viewed_auth.html', context)


def add_book_to_auth(request):
    print(request.POST)
    auth = Author.objects.get(id=request.POST['auth_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    auth.books.add(book)
    return redirect(f'/authors/{auth.id}')

from django.shortcuts import redirect, render
from .models import Books

from django.views.generic import ListView, DetailView


def index(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books': books})


def my_dashboard(request):
    books = Books.objects.all()
    return render(request, 'dash.html', {'books': books})


def add(request):
    return render(request, 'add.html')


def addrec(request):
    x = request.POST['book-title']
    y = request.POST['authors']
    z = request.POST['genres']
    k = request.POST['condition']
    l = request.POST['location']
    o = request.POST['owner']
    book = Books(title=x, authors=y, genres=z, condition=k, location=l, owner=o)

    book.save()
    return redirect("/dash")


def delete(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect("/dash")


def update(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'update.html', {'book': book})


def uprec(request, id):
    x = request.POST['book-title']
    y = request.POST['authors']
    z = request.POST['genres']
    k = request.POST['condition']
    l = request.POST['location']

    book = Books.objects.get(id=id)

    book.title = x
    book.authors = y
    book.genres = z
    book.condition = k
    book.location = l

    book.save()
    return redirect("/dash")


def search(request):
    books = Books.objects.all()
    return render(request, 'search.html', {'books': books})
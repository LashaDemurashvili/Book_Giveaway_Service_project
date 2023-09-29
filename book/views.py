from django.shortcuts import redirect, render
from .models import Books
from django.db.models import Q

from django.views.generic import ListView, DetailView


def index(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books': books})


def my_dashboard(request):
    books = Books.objects.all()
    return render(request, 'dash.html', {'books': books})


def add(request):
    return render(request, 'add.html')


# create new book
def addrec(request):
    x = request.POST['book-title']
    y = request.POST['authors']
    z = request.POST['genres']
    k = request.POST['condition']
    l = request.POST['location']
    o = request.POST['owner']
    book = Books(title=x, authors=y, genres=z, condition=k, location=l, owner=o)

    # save db
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


class Search(ListView):
    model = Books
    template_name = 'search.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        # return Books.objects.filter(title__icontains=query)

        # search with some arguments
        return Books.objects.filter(Q(title__icontains=query) | Q(authors__icontains=query) |
                                    Q(genres__icontains=query) | Q(condition__icontains=query) |
                                    Q(location__icontains=query) | Q(owner__icontains=query)
                                    )

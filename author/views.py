from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import action
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import Author

from .forms import *
from book.models import Book
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'author/authors.html', context)


def author_books(request, authorid):
    print(authorid)
    context = {
        'books': Book.objects.filter(authors=authorid),
        'author': Author.get_by_id(authorid)
    }
    return render(request, 'author/auth_books.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AddAuthorPostForm()
    return render(request, 'author/add_author.html', {'form': form})


def delete_author(request, authorid):
    print('DELETE')
    author = Author.objects.get(pk=authorid)
    author.delete()
    return redirect('authors')

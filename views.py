from django.shortcuts import render, redirect
from .models import Book, Category
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        messages.success(request, 'login required')
        return redirect('/users/login/')
    else:
        category = Category.objects.all()
        recommended_books = Book.objects.filter(recommended_books=True)
        fiction_books = Book.objects.filter(fiction_books=True)
        business_books = Book.objects.filter(business_books=True)
        return render(request, 'portfolio_filter.html', {'recommended_books': recommended_books,
                                             'business_books': business_books, 'fiction_books': fiction_books,
                                             'categories': category
                                             })
def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def all_books(request):
    category = Category.objects.all()
    book = Book.objects.all()
    context = {
            'book': book,
            'categories': category
        }
    return render(request, 'portfolio_filter.html', context)


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'genre_detail.html', {'category': category})


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith=book_category)
    return render(request, 'book_detail.html', {'book': book, 'similar_books': similar_books})


def search_book(request):
    searched_books = Book.objects.filter(title__icontains=request.POST.get('name_of_book'))
    return render(request, 'search_book.html', {'searched_books': searched_books})

def notes(request):
    if not request.user.is_authenticated:
        messages.success(request, 'login required')
        return redirect('/users/login/')
    else:
        category = NCategory.objects.all()
        recommended_books = Notes.objects.filter(recommended_books=True)
        fiction_books = Notes.objects.filter(fiction_books=True)
        business_books = Notes.objects.filter(business_books=True)
        return render(request, 'notes.html', {'recommended_books': recommended_books,
                                             'business_books': business_books, 'fiction_books': fiction_books,
                                             'categories': category
                                             })
def ncategory_links(request):
    category = NCategory.objects.all()
    return {'categories': category}

def search_notes(request):
    searched_notes = Notes.objects.filter(title__icontains=request.POST.get('name_of_subject'))
    return render(request, 'search_notes.html', {'searched_notes': searched_notes})


def ncategory_detail(request, slug):
    category = NCategory.objects.get(slug=slug)
    return render(request, 'genr.html', {'category': category})

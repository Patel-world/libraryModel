from django.urls import path
from . import views

urlpatterns = [
    path('home', views.all_books, name = 'home'),
    path('all_books', views.all_books, name = 'all_books'),
    path('genre/<str:slug>', views.category_detail, name = 'category_detail'),
    #path('pdf/<str:slug>', views.book_detail, name = 'book_detail'),
    path('searched_books', views.search_book, name = 'book_search'),
    path('exam-zone', views.notes, name='exam-zone'),
    path('searched_notes', views.search_notes, name = 'note_search'),
]
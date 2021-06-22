from .models import Category, NCategory
from .forms import BookSearchForm, NoteSearchForm

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def book_search(request):
    search_form = BookSearchForm
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}

def Ncategory_links(request):
    category = NCategory.objects.all()
    return {'categories': category}

def Nbook_search(request):
    search_form = NoteSearchForm
    if request.method == 'POST':
        search_form = NoteSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}
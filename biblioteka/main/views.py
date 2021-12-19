from django.shortcuts import render
from .models import Books
from .forms import BooksForm


def index(reqest):
    return render(reqest, 'main/index.html')

def about(reqest):
    return render(reqest, 'main/about.html')

def readers(reqest):
    return render(reqest, 'main/readers.html')

def search(reqest):
    if reqest.method == 'POST':
        form = BooksForm(reqest.POST)
        print(form)
    books = Books.objects.all()
    form = BooksForm()
    return render(reqest, 'main/search.html',{'title': 'Поиск книг','books': books, 'form': form})

def events(reqest):
    return render(reqest, 'main/events.html')


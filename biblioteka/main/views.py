from django.shortcuts import render
from .models import Books
from .forms import BooksForm


def index(reqest):
    return render(reqest, 'main/index.html')

def about(reqest):
    return render(reqest, 'main/about.html')

def readers(reqest):
    return render(reqest, 'main/readers.html')

def search(request):
    if request.method == 'POST':
        b = request.POST['title']
        print(b)
        books = Books.objects.get(title=b)
    else:
        books = Books.objects.all()
    form = BooksForm()
    #queryset = City.objects.filter(name__icontains='Boston')
    return render(request, 'main/search.html',{'title': 'Поиск книг','books': books, 'form': form})

def events(reqest):
    return render(reqest, 'main/events.html')


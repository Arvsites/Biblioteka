from .models import Books
from django.forms import ModelForm, TextInput


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора книги'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }),
        }
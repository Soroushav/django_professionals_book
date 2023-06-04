from .models import Book, Review
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookEditForm(ModelForm):
    class Meta:
        model = Book
        fields = ('tittle', 'author', 'price')


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

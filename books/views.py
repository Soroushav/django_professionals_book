from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from .forms import BookForm, BookEditForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from watson import search as watson


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books_list'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('home')
    form_class = BookForm
    login_url = 'account_login'


class BookEditView(LoginRequiredMixin, UpdateView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_edit.html'
    success_url = reverse_lazy('home')
    form_class = BookEditForm
    login_url = 'account_login'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'book'
    login_url = 'account_login'


class SearchResultsListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET['q']
        queryset = watson.filter(Book, query)
        return queryset
        # queryset = Book.objects.filter(
        #     Q(tittle__icontains=query) | Q(tittle__icontains=query)
        # )
        # return queryset

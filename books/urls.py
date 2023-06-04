from django.urls import path, include
from .views import BookListView, BookDetailView, BookCreateView, BookEditView, BookDeleteView, SearchResultsListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('edit/<uuid:pk>/', BookEditView.as_view(), name='book_edit'),
    path('delete/<uuid:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
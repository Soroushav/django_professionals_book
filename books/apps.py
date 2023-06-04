from django.apps import AppConfig
from watson import search as watson


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    def ready(self):
        Book = self.get_model('Book')
        watson.register(Book)

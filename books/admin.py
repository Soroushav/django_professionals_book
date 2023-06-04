from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    list_display = ['tittle', 'author', 'price']


admin.site.register(Book, BookAdmin)
admin.site.register(Review)

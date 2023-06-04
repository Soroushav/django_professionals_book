from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        # db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    tittle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ('special_status', 'Can Read All Books'),
        ]

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

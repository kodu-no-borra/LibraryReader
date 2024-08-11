from django.db import models
from apps.users.models import Reader
from simple_history.models import HistoricalRecords


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(
        Reader,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='borrowed_books'
    )
    borrowed_date = models.DateTimeField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


"""
class BorrowedBookRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.reader.user.get_full_name()} - {self.book.title}"

    class Meta:
        ordering = ['-borrowed_date']
"""
# Промежуточная таблица с инф для отслеживания юзера взявшего книгу

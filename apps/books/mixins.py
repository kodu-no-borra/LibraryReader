from django.utils import timezone
from apps.books.models import Book


class BorrowListMixin:
    def get_queryset(self):
        return Book.objects.filter(is_borrowed=True).select_related('borrowed_by')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = timezone.now()
        for book in context['list_borrow']:
            book.borrowed_duration = current_time - book.borrowed_date

            days = book.borrowed_duration.days
            hours, remainder = divmod(book.borrowed_duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            book.borrowed_duration = '{:d} дн {:02} ч {:02} мин'.format(days, hours, minutes)
        return context


"""
class BorrowBookMixin:

    def handle_borrow_or_return(self, book, reader, request):
        
        active_record = BorrowedBookRecord.objects.filter(book=book, reader=reader, returned_date__isnull=True).first()

        if active_record: # Если запись найденав - книга возвращается
            active_record.returned_date = timezone.now()
            active_record.save()
            messages.info(request, f'Вы успешно вернули книгу "{book.title}".')
            
        else:  # Если активной записи нет - создаем новую запись о взятии книги
            BorrowedBookRecord.objects.create(book=book, reader=reader)
            messages.success(request, f'Вы успешно взяли книгу "{book.title}".')

"""
# Миксин для обработки логики взятия и возврата книги читателем.
# Включает методы для создания записи о взятии книги и обновления записи о возврате книги.
# Если читатель уже взял книгу и возвращает её, обновляет запись и устанавливает дату возврата.
# Если читатель берет книгу впервые, создается новая запись.

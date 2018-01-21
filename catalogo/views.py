from django.shortcuts import render
from django.utils import timezone
from .models import Book
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    books = Book.objects.order_by('created_date')
    return render(request, 'catalogo/post_list.html',{'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalogo/book_detail.html', {'book': book})

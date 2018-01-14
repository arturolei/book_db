from django.shortcuts import render
from django.utils import timezone
from .models import Book

# Create your views here.
def post_list(request):
    books = Book.objects.order_by('created_date')
    return render(request, 'catalogo/post_list.html',{'books': books})

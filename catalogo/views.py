from django.shortcuts import render
from django.utils import timezone
from .models import Book
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
    books = Book.objects.order_by('created_date')
    return render(request, 'catalogo/post_list.html',{'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalogo/book_detail.html', {'book': book})

def book_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'catalogo/book_edit.html', {'form': form})

def book_edit(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'catalogo/book_edit.html', {'form': form})

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Max, Min

from .models import Book

def index(request):
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    print(books)
    return render(request, "bookstore/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "bookstore/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })

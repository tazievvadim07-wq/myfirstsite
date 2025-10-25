from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Author, Tag, Book

def index(request):
    return HttpResponse("Это блог-раздел моего сайта")

def book_list(request):
    books_expensive = Book.objects.filter(price__gt=2000)
    books_recent = Book.objects.filter(year__gt=2010).order_by("year")
    books_tolstoy = Book.objects.filter(author__icontains="Толстой")

    context = {
        "books_expensive": books_expensive,
        "books_recent": books_recent,
        "books_tolstoy": books_tolstoy,
    }
    return render(request, "blog/book_list.html", context)


def search_view(request):
    query = request.GET.get("q", "")  # получаем текст из формы
    results = []

    if query:
        results = Book.objects.filter(author__icontains=query)

    context = {
        "query": query,
        "results": results,
    }
    return render(request, "blog/search.html", context)
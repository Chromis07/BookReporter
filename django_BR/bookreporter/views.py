from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, render, resolve_url

from bookreporter.models import Book, Review, Quote

def book_list(request):
    qs = Book.objects.all()
    return render(request, "bookreporter/book_list.html", {
        "book_list" : qs,
    })
    

def book_detail(request, pk):
    book = Book.objects.all(pk=pk)
    return render(request, "bookreporter/book_detail.html", {
        "book" : book,
    })
    
    
    
# review 쓰기 + quote 쓰기

def review_new():
    pass

def review_edit():
    pass

def review_delete():
    pass

def quote_new():
    pass

def quote_edit():
    pass

def quote_delete():
    pass
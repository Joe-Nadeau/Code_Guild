from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, author, book_status

# Create your views here.

def display_homepage(request):
    return render(request, "landing_page.html")

def check_out_books(request):
    books = Book.objects.all()
    return render(request, "books.html")

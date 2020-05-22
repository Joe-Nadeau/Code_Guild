from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, author, book_status

# Create your views here.

def display_homepage(request):
    return render(request, "landing_page.html")

def check_out_books(request):
    books = Book.objects.all()
    status = book_status.objects.all()

    context = {
        'books': books,
        'status': status,
    }

    return render(request, 'books.html', context) # context is sent to 'books.html'

def add_book(request, id):
    return render(request, "landing_page.html")

def return_book(request, id):
    return render(request, "landing_page.html")


# def remove(request, id):
#     todo_item = TodoItem.objects.get(id = id)
#     todo_item.delete()
#     return redirect('todo_list')
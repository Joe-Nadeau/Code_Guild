from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, author

# Create your views here.

def display_homepage(request):
    return render(request, "landing_page.html")

def check_out_books(request):
    books = Book.objects.all()
    
    context = {
        'books': books,
    }

    return render(request, 'books.html', context) # context is sent to 'books.html'

def loan_book(request, id):
    book = Book.objects.get(id = id)
    book.check_out(request.user)
    book.save()
    return redirect('profile')

def return_book(request, id):
    book = Book.objects.get(id = id)
    book.check_in()
    book.save()
    return redirect('profile')




# def remove(request, id):
#     todo_item = TodoItem.objects.get(id = id)
#     todo_item.delete()
#     return redirect('todo_list')
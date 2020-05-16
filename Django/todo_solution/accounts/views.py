from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

def login_user(request):
    username = request.POST.get('InputUsername')
    password = request.POST.get('InputPassword1')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'todos/list.html' )
    else:
        return render(request, 'accounts/login.html')

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
        ...

def logout_user(request):
    logout(request)
    return redirect('home')

# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
User = get_user_model()
# creates new user
def register_new_user(request):
    if request.method == 'POST':
        new_user = User(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        username = request.POST['username'],
        email = request.POST['email'],
        )

        password = request.POST['password']
        new_user.set_password(password)
        new_user.save()

        return redirect('list')
    
    else:
        return render(request, 'accounts/register.html')

# # view add a todo to the database. this view handles both GET and POST HTTP requests
# def add_todo(request):
#     if request.method == 'GET': # if its a GET request, just display the todos/add.html template
#         return render(request, 'todos/add.html')
#     elif request.method == 'POST': # if it's a POST request ...
#         title = request.POST['title']   # get the title from the POST submission, this comes form a form
#         text = request.POST['text']     # get the text from the POST submission, this comes form a form
#         if (request.POST['status'] == 'False'): # check the status because it's a string and booleans are not strings
#             status = False
#         else:
#             status = True
#         # add the new todo to the databse. objects.create() automatically saves the new todo for us so we
#         # don't need a separate call to the save() method
#         todo = Todo.objects.create(title = title, text = text, status = status)
#         return redirect('list')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate
from iEaccounts.models import Users, Profiles

# Create your views here.

def login_user(request):
    username = request.POST.get('InputUsername')
    password = request.POST.get('InputPassword1')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home_page.html' )
    else:
        return render(request, 'iEaccounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('ironenclave:home/')

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

        return redirect('iEcommunity:home_page')
    else:
        return render(request, 'iEaccounts/register.html')

def user_profile(request):
    return render(request, 'iEaccounts/profile.html')
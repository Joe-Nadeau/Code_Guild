from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate
from iEaccounts.models import Profiles
from iEgraph.models import Graph
from bokeh.plotting import figure, output_file, show, save
from bokeh.resources import CDN
from bokeh.embed import components, file_html

User = get_user_model()

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('InputUsername')
        password = request.POST.get('InputPassword1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home_page.html' )
        else:
            return redirect('iEaccounts:login_page')
    else:
        return render(request, 'iEaccounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('iEcommunity:home_page')


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

        new_profile = Profiles(
        user = new_user,
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        )

        new_profile.save()

        return redirect('iEcommunity:home_page')
    else:
        return render(request, 'iEaccounts/register.html')

def user_profile(request):
    prof_mod = Profiles.objects.get(user = request.user)
    graph_mod = Graph.objects.filter(user = request.user)

    plot = figure()
    plot.circle([1,2], [3,4])

    output_file("test.html")
    save(plot)

    context = {
        'prof_mod': prof_mod,
        'graph_mod': graph_mod,
    }

    return render(request, 'iEaccounts/profile.html', context)

# POST-Updating profile
def update_profile(request, id):
    if request.method == 'POST':
        
        profile = Profiles.objects.get(user = User.objects.get(id = id))
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.age = request.POST['age']
        profile.profile_img = request.FILES.get('profile_img')
        profile.bio = request.POST['bio']
        profile.gender = request.POST['gender']
        profile.weight_class = request.POST['weight_class']

        profile.save()

        return redirect('iEaccounts:profile')

    else:
        user = User.objects.get(id = id)
        profile = Profiles.objects.get(user = User.objects.get(id = id))
        print(profile.weight_class_choices[0])
        context = {
            'user': user,
            'profile': profile,
            'weight_class': Profiles.weight_class_choices,
        }
        return render(request, 'iEaccounts/update_profile.html', context)

def update_graph(request):
    if request.method == 'POST':

        weight = request.POST['weight']
        lift = request.POST['lift']

        return redirect('iEaccounts:profile')


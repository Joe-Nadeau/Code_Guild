from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, "landing_page.html")

def home_page(request):
    return render(request, "home_page.html")

def resources(request):
    return render(request, "resources.html")

def forum_main(request):
    return render(request, "iEcommunity/forum_main.html")
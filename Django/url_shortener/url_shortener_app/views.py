from django.shortcuts import render, redirect
import random
import string
from .models import Model_U


# Create your views here.

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('user_url')
        new_url = Model_U.objects.create(url = long_url, url_hash = gen_rand())
        return redirect('index')
    else:
        URLS = Model_U.objects.all()
        return render(request, 'index.html', {'URLS': URLS})

def gen_rand():
    url_hash = []
    for i in range(20):
        url_hash.append(random.choice(string.printable))
    return "".join(url_hash)

def delete_url(request, id):
    trash_urls = Model_U.objects.get(id = id)
    trash_urls.delete()
    return redirect('index')

# one_entry = Entry.objects.get(pk=1)
# def remove(request, id):
#     todo_item = TodoItem.objects.get(id = id)
#     todo_item.delete()
#     return redirect('todo_list')
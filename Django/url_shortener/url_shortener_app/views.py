from django.shortcuts import render, redirect
import random
import string
from .models import Model_U


# Create your views here.

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('user_url')
        Model_U.objects.create(url = long_url, url_hash = gen_rand())
        return redirect('index')
    else:
        URLS = Model_U.objects.all()
        return render(request, 'index.html', {'URLS': URLS})
    # todo_items = TodoItem.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    # return render(request, 'todo_list.html', {'todo_items': todo_items})

        

    # user_input = request.POST["new_task"]
    # TodoItem.objects.create(task_description = user_input, created_date = timezone.now())
# def password_picker(lc_count, uc_count, dig_count, spec_count, password):
#     for i in range(0, lc_count):
#         password.append(random.choice(string.ascii_lowercase))
#     for i in range(0, uc_count):
#         password.append(random.choice(string.ascii_uppercase))
#     for i in range(0, dig_count):
#         password.append(random.choice(string.digits))
#     for i in range(0, spec_count):
#         password.append(random.choice(string.punctuation))
#     random.shuffle(password)
#     passtring = ''.join(password)
#     print(passtring)

def gen_rand():
    url_hash = []
    for i in range(20):
        url_hash.append(random.choice(string.printable))
    return url_hash



def return_shorty(request):
    pass
    # performs the redirecting (localhost/redirect/pEc4vt), you should use redirect instead of HttpResponseRedirect.

    #     if request.method == 'POST':
        #     task_description = request.POST.get('task_description')
        #     todo_item.task_description = task_description
        #     todo_item.save()
        #     return redirect('todo_list')
    # else:
    #     todo_item = TodoItem.objects.get(id = id)
    #     context = {
    #         'todo_item': todo_item,
    #     }
    #     return render(request, 'edit.html', context)


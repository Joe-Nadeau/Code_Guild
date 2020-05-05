from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TodoItem
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def todo_list(request):
    todo_items = TodoItem.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo_list.html', {'todo_items': todo_items})

def detail(request, id):
    todo_item = TodoItem.objects.get(id = id)
    todo_items = TodoItem.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    context = {
        'todo_item': todo_item, 
        'todo_items': todo_items,
    }
    return render(request, 'detail.html', context)

def remove(request, id):
    todo_item = TodoItem.objects.get(id = id)
    todo_item.delete()
    return redirect('todo_list')

def update(request, id):
    if request.method == 'POST':
        print("Anything goes here")
        todo_item = TodoItem.objects.get(id = id)
        if (request.POST.get('check_box', False)) == 'on':
            # todo_item.is_completed = True
            todo_item.complete_task()
        task_description = request.POST.get('task_description')
        todo_item.task_description = task_description
        todo_item.save()
        return redirect('todo_list')
    else:
        todo_item = TodoItem.objects.get(id = id)
        context = {
            'todo_item': todo_item,
        }
        return render(request, 'edit.html', context)

def new_task(request):
    user_input = request.POST["new_task"]
    TodoItem.objects.create(task_description = user_input, created_date = timezone.now())
    return redirect('todo_list')

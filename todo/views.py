from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import TodoItem

# Create your views here.


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

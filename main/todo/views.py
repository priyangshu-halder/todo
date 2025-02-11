from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm

def delete(request, pk):
    item=Task.objects.get(unique_id=pk)
    item.delete()
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = TaskForm()

    if request.method=='delete':
        d=delete()
        return d
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}

    return render(request, 'todo/index.html', context)
def edit(request, pk):
    item=Task.objects.get(unique_id=pk)
    form=TaskForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    context={'form':form}
    return render(request, 'todo/edit.html', context)
def delete(request, pk):
    item=Task.objects.get(unique_id=pk)
    item.delete()
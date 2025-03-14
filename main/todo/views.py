from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = TaskForm()

    tasks = .objects.all()
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
    if request.method=='POST':
        item.delete()
        return redirect('index')
    context={'item':item}
    return render(request, 'todo/delete.html', context)
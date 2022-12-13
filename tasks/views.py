from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator  #lib para paginação
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def taskList(request):

    search = request.GET.get('search')
    
    if search:
        tasks = Task.objects.filter(title__icontains=search)    #filtro busca
    else:            
        tasks_list = Task.objects.all().order_by('-created_at')  
            
        paginator = Paginator(tasks_list, 3)
        
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
        
    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def newTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            
            messages.info(request, 'Tarefa criada com sucesso.')
            return redirect('/')
            
    else:        
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})
    

@login_required    
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)   #para listar a task específica
    
    if(request.method == "POST"):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            
            messages.info(request, 'Tarefa editada com sucesso.')
            return redirect('/')
        else:            
            return render(request, 'tasks/edittask.html', {'form': form, 'taks': task})
    else:        
        return render(request, 'tasks/edittask.html', {'form': form, 'taks': task})
    

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    
    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')




def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
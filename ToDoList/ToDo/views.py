from .models import Task
from django.shortcuts import render
from django.http import HttpResponse

def toDo(request):
	tasks = Task.objects.all()[:10]
	context = {
	'title' :'Uncompleted tasks',
	'tasks' : tasks
	}
	return render(request, 'ToDo/toDo.html', context)
def details(request,id):
	task =  Task.objects.get(id=id)
	context = {
	'Task' : task
	}
	return render(request, 'ToDo/details.html', context)

def index(request):
	return render(request,'ToDo/index.html')
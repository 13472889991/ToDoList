from .models import Task
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout


def toDo(request):
	tasks = Task.objects.all()[:10]
	context = {
	'title' :'Uncompleted tasks',
	'tasks' : tasks
	}
	if request.user.is_authenticated:
		user = request.user
		context['user'] = user.username
	else:
		context['user'] = "Not currently logged in"
	return render(request, 'ToDo/toDo.html', context)
def details(request,id):
	task =  Task.objects.get(id=id)
	context = {
	'Task' : task
	}
	return render(request, 'ToDo/details.html', context)
def logout(request):
	logout(request)
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/ToDo')
	else:
		form = UserCreationForm()
	return render(request, 'ToDo/signup.html', {'form': form})
def index(request):
	if request.user.is_authenticated:
		context = {
		'login' : request.user.username
		}
	else:
		context = {
		'login' : 'Login/Signup'
		}
	return render(request,'ToDo/index.html',context)
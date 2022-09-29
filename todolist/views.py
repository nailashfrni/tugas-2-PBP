from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from todolist.models import Task
# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user
    todolist = Task.objects.filter(user=username)
    
    for todo in todolist:
        if todo.is_finished == True:
            todo.is_finished = 'Selesai'
        else:
            todo.is_finished = 'Belum Selesai'

    context = {
        "todolist": todolist,
        "username": username,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil menambahkan task!')
            return redirect('todolist:show_todolist')

    context = {"form":form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

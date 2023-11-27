from django.shortcuts import render,redirect,get_object_or_404
from todoapp.models import todo
from todoapp.forms import todo_form

# Create your views here.

def retriveview(request):
    task = todo.objects.all()
    return render(request, 'todoapp/index.html',{'task':task})

def createview(request):
    forms = todo_form()
    if request.method =='POST':
        forms = todo_form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
        
    return render(request, 'todoapp/create.html',{'form':forms})

def deleteview(request, pk_id):
    #task = todo.objects.get(id=id)
    task = get_object_or_404(todo, pk=pk_id)
    task.delete()
    return redirect('/')

def updateview(request, pk_id):
    #task = todo.objects.get(id=id)
    task = get_object_or_404(todo, id=pk_id)
    if request.method =='POST':
        forms = todo_form(request.POST,instance = task)
        if forms.is_valid():
            forms.save()
            return redirect('/')
               
    return render(request, 'todoapp/update.html',{'task':task})
